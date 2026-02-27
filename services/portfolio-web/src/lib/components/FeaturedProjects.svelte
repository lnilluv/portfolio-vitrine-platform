<script lang="ts">
  import type { ProjectCard } from "$lib/types";

  export let projects: ProjectCard[] = [];

  const featured = projects.slice(0, 3);
</script>

<section class="featured-section">
  <div class="section-head">
    <p class="eyebrow">Featured Projects</p>
    <h2>Selected builds with measurable outcomes</h2>
  </div>
  <div class="featured-grid">
    {#each featured as project}
      <article class="card featured-card">
        <p class="pill">{project.runtime_mode}</p>
        <h3>{project.title}</h3>
        <p>{project.business_problem}</p>
        <div class="links">
          <a class="button button-secondary" href={project.live_url} target="_blank" rel="noreferrer">Live Demo</a>
          <a class="button button-secondary" href={project.repo_url} target="_blank" rel="noreferrer">Repository</a>
        </div>
      </article>
    {/each}
  </div>
</section>

<style>
  .featured-section {
    margin: 2.2rem 0;
  }

  .section-head h2 {
    margin-top: 0.5rem;
    font-size: clamp(1.4rem, 3vw, 2rem);
    max-width: 24ch;
  }

  .featured-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.8rem;
    margin-top: 0.95rem;
  }

  .featured-card {
    padding: 1rem;
    display: grid;
    gap: 0.65rem;
  }

  .featured-card h3 {
    font-size: 1.16rem;
  }

  .featured-card p {
    color: var(--ink-soft);
    line-height: 1.5;
  }

  .links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 0.4rem;
  }

  @media (max-width: 940px) {
    .featured-grid {
      grid-template-columns: 1fr;
    }
  }
</style>
