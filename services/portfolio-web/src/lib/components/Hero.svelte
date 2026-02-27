<script lang="ts">
  export let projectCount = 0;
</script>

<section id="hero" class="hero">
  <div class="hero-copy">
    <p class="eyebrow">ML Engineer and Data Product Builder</p>
    <h1>From experimental models to reliable products on constrained infrastructure.</h1>
    <p class="hero-description">
      I design and ship portfolio-grade systems that combine machine learning, API delivery,
      and practical MLOps execution.
    </p>
    <div class="hero-actions">
      <a class="button button-primary" href="#all-projects">View Projects</a>
      <a class="button button-secondary" href="mailto:hello@portfolio.local">Contact</a>
    </div>
  </div>
  <aside class="hero-stats card" aria-label="portfolio metrics">
    <h2>Portfolio Snapshot</h2>
    <ul>
      <li><strong>{projectCount}</strong> showcased projects</li>
      <li><strong>3</strong> runtime profiles</li>
      <li><strong>1</strong> unified metadata source</li>
    </ul>
  </aside>
</section>

<style>
  .hero {
    display: grid;
    grid-template-columns: 1.15fr minmax(240px, 0.85fr);
    gap: 1rem;
    align-items: end;
    margin-bottom: 1.6rem;
  }

  .hero-copy {
    padding: 0.8rem 0 1rem;
  }

  .hero h1 {
    font-size: clamp(2rem, 5.6vw, 4rem);
    margin: 0.6rem 0 0.8rem;
    max-width: 17ch;
  }

  .hero-description {
    max-width: 58ch;
    line-height: 1.6;
    color: var(--ink-soft);
  }

  .hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
    margin-top: 1.25rem;
  }

  .hero-stats {
    padding: 1rem;
    transform: rotate(-1deg);
  }

  .hero-stats h2 {
    font-size: 1.2rem;
    margin-bottom: 0.75rem;
  }

  .hero-stats ul {
    margin: 0;
    padding: 0;
    list-style: none;
    display: grid;
    gap: 0.45rem;
    color: var(--ink-soft);
  }

  .hero-stats strong {
    color: var(--ink);
  }

  @media (max-width: 860px) {
    .hero {
      grid-template-columns: 1fr;
    }

    .hero-stats {
      transform: none;
      max-width: 400px;
    }
  }
</style>
