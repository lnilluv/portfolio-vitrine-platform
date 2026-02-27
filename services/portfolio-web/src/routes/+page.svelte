<script lang="ts">
  import FeaturedProjects from "$lib/components/FeaturedProjects.svelte";
  import Hero from "$lib/components/Hero.svelte";
  import ProjectGrid from "$lib/components/ProjectGrid.svelte";
  import ProjectModal from "$lib/components/ProjectModal.svelte";
  import TrustStrip from "$lib/components/TrustStrip.svelte";
  import type { LoaderState, ProjectCard } from "$lib/types";

  export let data: LoaderState;

  let selectedMode = "all";
  let selectedSkill = "all";
  let selectedProject: ProjectCard | null = null;

  const projects = data.projects ?? [];
</script>

<main class="page-shell">
  <section id="hero">
    <Hero projectCount={projects.length} />
  </section>
  <TrustStrip />

  {#if data.errorMessage}
    <section id="catalog-fallback" class="card fallback" role="status">
      <p class="eyebrow">Catalog Status</p>
      <h2>Project catalog temporarily unavailable</h2>
      <p>{data.errorMessage}</p>
      <a class="button button-secondary" href="#all-projects">Retry by reloading</a>
    </section>
  {/if}

  <section id="featured-projects">
    <FeaturedProjects projects={projects} />
  </section>

  <section id="all-projects">
    <ProjectGrid
      projects={projects}
      onSelect={(project) => (selectedProject = project)}
      {selectedMode}
      {selectedSkill}
      onModeChange={(value) => (selectedMode = value)}
      onSkillChange={(value) => (selectedSkill = value)}
    />
  </section>

  <footer class="footer card">
    <p class="eyebrow">Availability</p>
    <p>Open to remote ML engineering and data platform roles.</p>
    <div class="footer-links">
      <a href="https://github.com/lnilluv" target="_blank" rel="noreferrer">GitHub</a>
      <a href="mailto:hello@portfolio.local">Email</a>
    </div>
  </footer>
</main>

<ProjectModal project={selectedProject} onClose={() => (selectedProject = null)} />

<style>
  .fallback {
    padding: 1rem;
    margin: 1.8rem 0;
    display: grid;
    gap: 0.55rem;
  }

  .fallback h2 {
    font-size: 1.4rem;
  }

  .fallback p {
    color: var(--ink-soft);
    line-height: 1.55;
  }

  .footer {
    margin-top: 2.4rem;
    padding: 1rem;
    display: grid;
    gap: 0.6rem;
  }

  .footer-links {
    display: flex;
    gap: 0.8rem;
    font-weight: 700;
  }
</style>
