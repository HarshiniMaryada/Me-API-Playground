from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import sqlite3, json, os

app = FastAPI(title="Me-API Playground")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

DB_PATH = "profile.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# ---------------------------
# Pydantic model for profile update
# ---------------------------
class ProfileUpdate(BaseModel):
    name: str = None
    email: str = None
    education: str = None
    skills: list = []
    work: list = []
    projects: list = []
    links: dict = {}

# ---------------------------
# Routes
# ---------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/profile")
def get_profile():
    conn = get_db()
    row = conn.execute("SELECT * FROM profile WHERE id=1").fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Profile not found")
    data = dict(row)
    for k in ["skills", "projects", "work", "links"]:
        data[k] = json.loads(data[k])
    return data

@app.post("/profile")
@app.patch("/profile")
def update_profile(profile: ProfileUpdate, request: Request):
    auth_key = os.environ.get("WRITE_API_KEY")
    if auth_key and auth_key not in (request.headers.get("Authorization") or ""):
        raise HTTPException(status_code=401, detail="Unauthorized")

    conn = get_db()
    conn.execute("""
        UPDATE profile SET
        name=?, email=?, education=?, skills=?, work=?, projects=?, links=?, updated_at=CURRENT_TIMESTAMP
        WHERE id=1
    """, (
        profile.name,
        profile.email,
        profile.education,
        json.dumps(profile.skills),
        json.dumps(profile.work),
        json.dumps(profile.projects),
        json.dumps(profile.links)
    ))
    conn.commit()
    conn.close()
    return {"updated": True}

@app.get("/projects")
def projects(skill: str = ""):
    conn = get_db()
    row = conn.execute("SELECT projects FROM profile WHERE id=1").fetchone()
    conn.close()
    projects = json.loads(row["projects"])
    if skill:
        s = skill.lower()
        projects = [p for p in projects if s in p["title"].lower() or s in p["description"].lower()]
    return projects

@app.get("/skills/top")
def top_skills():
    conn = get_db()
    row = conn.execute("SELECT skills FROM profile WHERE id=1").fetchone()
    conn.close()
    return json.loads(row["skills"])

@app.get("/search")
def search(q: str = ""):
    q = q.lower()
    conn = get_db()
    row = conn.execute("SELECT * FROM profile WHERE id=1").fetchone()
    conn.close()
    if not row:
        return {"results": []}
    data = dict(row)
    results = []
    skills = json.loads(data["skills"])
    projects = json.loads(data["projects"])
    if q in (data["name"] or "").lower():
        results.append({"type": "profile", "item": data["name"]})
    results += [{"type": "skill", "item": s} for s in skills if q in s.lower()]
    results += [{"type": "project", "item": p["title"]} for p in projects if q in p["title"].lower()]
    return {"results": results}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
