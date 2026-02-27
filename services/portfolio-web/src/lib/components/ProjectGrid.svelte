<script lang="ts">
  import type { ProjectCard } from "$lib/types";

  export let projects: ProjectCard[] = [];
  export let onSelect: (project: ProjectCard) => void;
  export let selectedMode = "all";
  export let selectedSkill = "all";
  export let onModeChange: (value: string) => void;
  export let onSkillChange: (value: string) => void;

  $: modes = ["all", ...new Set(projects.map((project) => project.runtime_mode))];
  $: skills = ["all", ...new Set(projects.flatMap((project) => project.skills))];
  $: filtered = projects.filter((project) => {
    const modeMatch = selectedMode === "all" || project.runtime_mode === selectedMode;
    const skillMatch = selectedSkill === "all" || project.skills.includes(selectedSkill);
    return modeMatch && skillMatch;
  });
</script>

<section class="projects-section">
  <div class="section-head">
    <p class="eyebrow">Project Catalog</p>
    <h2>Explore by runtime profile and capability</h2>
  </div>
  <div class="filters card">
    <label>
      Runtime Mode
      <select value={selectedMode} on:change={(event) => onModeChange((event.target as HTMLSelectElement).value)}>
        {#each modes as mode}
          <option value={mode}>{mode}</option>
        {/each}
      </select>
    </label>
    <label>
      Skill
      <select value={selectedSkill} on:change={(event) => onSkillChange((event.target as HTMLSelectElement).value)}>
        {#each skills as skill}
          <option value={skill}>{skill}</option>
        {/each}
      </select>
    </label>
  </div>
  <div class="grid" role="list">
    {#if filtered.length === 0}
      <p>No projects match the selected filters.</p>
    {/if}
    {#each filtered as project}
      <article class="card grid-card" role="listitem">
        <p class="pill">{project.runtime_mode}</p>
        <h3>{project.title}</h3>
        <p>{project.business_problem}</p>
        <button type="button" class="button button-secondary" on:click={() => onSelect(project)}>
          Open details
        </button>
      </article>
    {/each}
  </div>
</section>

<style>
  .projects-section {
    margin-top: 2.2rem;
  }

  .section-head h2 {
    margin-top: 0.5rem;
    font-size: clamp(1.4rem, 3vw, 2rem);
  }

  .filters {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.8rem;
    padding: 0.9rem;
    margin-top: 0.95rem;
  }

  label {
    display: grid;
    gap: 0.4rem;
    font-size: 0.78rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 700;
    color: var(--ink-soft);
  }

  select {
    border-radius: 10px;
    border: 1px solid var(--line);
    background: rgba(255, 255, 255, 0.74);
    color: var(--ink);
    padding: 0.64rem 0.7rem;
    font-size: 0.88rem;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 0.8rem;
    margin-top: 0.9rem;
  }

  .grid-card {
    padding: 0.9rem;
    display: grid;
    gap: 0.65rem;
  }

  .grid-card h3 {
    font-size: 1.08rem;
  }

  .grid-card p {
    color: var(--ink-soft);
    line-height: 1.5;
  }

  @media (max-width: 700px) {
    .filters {
      grid-template-columns: 1fr;
    }
  }
</style>
