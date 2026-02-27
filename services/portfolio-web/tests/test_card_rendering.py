from pathlib import Path
import unittest


class CardRenderingTest(unittest.TestCase):
    def test_sveltekit_scaffold_exists(self) -> None:
        self.assertTrue(Path("services/portfolio-web/package.json").exists())
        self.assertTrue(Path("services/portfolio-web/svelte.config.js").exists())
        self.assertTrue(Path("services/portfolio-web/vite.config.ts").exists())
        self.assertTrue(Path("services/portfolio-web/src/app.html").exists())
        self.assertTrue(Path("services/portfolio-web/src/routes/+page.svelte").exists())

    def test_legacy_static_assets_removed(self) -> None:
        self.assertFalse(Path("services/portfolio-web/index.html").exists())
        self.assertFalse(Path("services/portfolio-web/assets/app.js").exists())
        self.assertFalse(Path("services/portfolio-web/assets/styles.css").exists())

    def test_server_loader_uses_projects_api(self) -> None:
        loader_content = Path(
            "services/portfolio-web/src/routes/+page.server.ts"
        ).read_text(encoding="utf-8")
        config_content = Path(
            "services/portfolio-web/src/lib/config.ts"
        ).read_text(encoding="utf-8")
        self.assertIn("PORTFOLIO_API_BASE", config_content)
        self.assertIn("/projects", loader_content)
        self.assertIn("fetch", loader_content)

    def test_page_contains_editorial_sections(self) -> None:
        page_content = Path(
            "services/portfolio-web/src/routes/+page.svelte"
        ).read_text(encoding="utf-8")
        hero_content = Path(
            "services/portfolio-web/src/lib/components/Hero.svelte"
        ).read_text(encoding="utf-8")
        self.assertIn('id="hero"', page_content)
        self.assertIn('id="featured-projects"', page_content)
        self.assertIn('id="all-projects"', page_content)
        self.assertIn('id="catalog-fallback"', page_content)
        self.assertIn("View Projects", hero_content)


if __name__ == "__main__":
    unittest.main()
