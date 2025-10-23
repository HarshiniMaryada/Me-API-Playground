import sqlite3

def init_db():
    conn = sqlite3.connect("profile.db")
    cur = conn.cursor()
    with open("schema.sql") as f:
        cur.executescript(f.read())
    with open("seed_profile.sql") as f:
        cur.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database created and seeded successfully.")

if __name__ == "__main__":
    init_db()
