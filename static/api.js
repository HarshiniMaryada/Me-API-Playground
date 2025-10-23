const BASE = "http://127.0.0.1:8000";

async function loadProfile() {
  const res = await fetch(BASE + "/profile");
  const p = await res.json();
  const div = document.getElementById("profile");
  div.innerHTML = `
    <h2>${p.name}</h2>
    <p>${p.email}</p>
    <p> ${p.education}</p>
    <h3>Skills</h3>
    ${p.skills.map(s => `<button onclick="loadProjects('${s}')">${s}</button>`).join(" ")}
    <h3>Links</h3>
    ${Object.entries(p.links).map(([k,v]) => `<a href="${v}" target="_blank">${k}</a>`).join("<br>")}
  `;
}

async function loadProjects(skill) {
  const res = await fetch(BASE + "/projects" + (skill ? `?skill=${skill}` : ""));
  const list = await res.json();
  const div = document.getElementById("projects");
  div.innerHTML = list.map(p => `
    <div class="project">
      <h4>${p.title}</h4>
      <p>${p.description}</p>
      ${p.links.map(l => `<a href="${l}" target="_blank">${l}</a>`).join("<br>")}
    </div>
  `).join("");
}

async function doSearch() {
  const q = document.getElementById("query").value;
  const res = await fetch(BASE + "/search?q=" + q);
  const r = await res.json();
  document.getElementById("searchResults").innerHTML =
    r.results.map(x => `<div><b>${x.type}</b>: ${x.item}</div>`).join("");
}

loadProfile();
loadProjects();
