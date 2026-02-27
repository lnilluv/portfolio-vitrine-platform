async function loadProjects() {
  const target = document.getElementById("cards");
  if (!target) {
    return;
  }

  const host = window.location.hostname.replace(/^www\./, "");
  const fallbackBase = host === "localhost" ? "http://127.0.0.1:8000" : `https://api.${host}`;
  const apiBase = window.PORTFOLIO_API_BASE || fallbackBase;
  const response = await fetch(`${apiBase}/projects`);
  if (!response.ok) {
    throw new Error(`API request failed with status ${response.status}`);
  }
  const projects = await response.json();

  target.innerHTML = "";
  projects.forEach((project) => {
    const article = document.createElement("article");
    article.className = "card";
    article.innerHTML = `
      <span class="badge">${project.runtime_mode}</span>
      <h2>${project.title}</h2>
      <p>${project.business_problem}</p>
      <p><strong>Skills:</strong> ${project.skills.join(", ")}</p>
      <p class="links"><a href="${project.live_url}" target="_blank" rel="noreferrer">Open showcase</a> <a href="${project.repo_url}" target="_blank" rel="noreferrer">Source code</a></p>
    `;
    target.appendChild(article);
  });
}

loadProjects().catch((error) => {
  const target = document.getElementById("cards");
  if (target) {
    target.innerHTML = `<p>Unable to load projects: ${error.message}</p>`;
  }
});
