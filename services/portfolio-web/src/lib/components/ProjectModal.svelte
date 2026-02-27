<script lang="ts">
  import type { ProjectCard } from "$lib/types";

  export let project: ProjectCard | null = null;
  export let onClose: () => void;
</script>

{#if project}
  <div class="overlay" role="presentation" on:click={onClose}></div>
  <div class="modal card" role="dialog" aria-modal="true" aria-label="project details">
    <button class="close" type="button" on:click={onClose} aria-label="Close project details">x</button>
    <p class="pill">{project.runtime_mode}</p>
    <h3>{project.title}</h3>
    <p class="description">{project.business_problem}</p>
    <p><strong>Stack:</strong> {project.stack.join(", ")}</p>
    <p><strong>Skills:</strong> {project.skills.join(", ")}</p>
    <div class="links">
      <a class="button button-primary" href={project.live_url} target="_blank" rel="noreferrer">Open demo</a>
      <a class="button button-secondary" href={project.repo_url} target="_blank" rel="noreferrer">View repo</a>
    </div>
  </div>
{/if}

<style>
  .overlay {
    position: fixed;
    inset: 0;
    z-index: 9;
    background: rgba(7, 15, 18, 0.45);
  }

  .modal {
    position: fixed;
    z-index: 10;
    right: max(1rem, calc((100vw - 1120px) / 2));
    top: 1rem;
    width: min(450px, calc(100vw - 2rem));
    padding: 1rem;
    display: grid;
    gap: 0.7rem;
  }

  .close {
    justify-self: end;
    border: 1px solid var(--line);
    background: rgba(255, 255, 255, 0.85);
    border-radius: 8px;
    width: 32px;
    height: 32px;
    cursor: pointer;
  }

  .modal h3 {
    font-size: 1.4rem;
  }

  .description {
    color: var(--ink-soft);
    line-height: 1.6;
  }

  .links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
  }

  @media (max-width: 700px) {
    .modal {
      top: auto;
      bottom: 0.75rem;
      right: 1rem;
    }
  }
</style>
