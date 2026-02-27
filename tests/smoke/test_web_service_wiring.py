from pathlib import Path
import unittest


class WebServiceWiringTest(unittest.TestCase):
    def test_web_service_uses_sveltekit_container(self) -> None:
        compose = Path("docker-compose.base.yml").read_text(encoding="utf-8")
        self.assertIn("services/portfolio-web/Dockerfile", compose)
        self.assertIn("PORTFOLIO_API_BASE", compose)
        self.assertIn("loadbalancer.server.port=4173", compose)


if __name__ == "__main__":
    unittest.main()
