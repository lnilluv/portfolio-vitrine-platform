async function loadProjects() {
  const target = document.getElementById("cards");
  if (!target) {
    return;
  }

  const fallbackBase = window.location.origin.replace("portfolio", "api.portfolio");
  const apiBase = window.PORTFOLIO_API_BASE || fallbackBase;
  const response = await fetch(`${apiBase}/projects`);
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
      <p><a href="${project.live_url}" target="_blank" rel="noreferrer">Open showcase</a></p>
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
