from pathlib import Path
import unittest


class NlpServiceIntegrationTest(unittest.TestCase):
    def test_nlp_service_registered_in_demo_compose(self) -> None:
        compose_text = Path("docker-compose.demos.yml").read_text(encoding="utf-8")
        self.assertIn("nlp-spam-api", compose_text)
        self.assertIn("SPAM_HOST", compose_text)
        self.assertTrue(Path("services/integrations/nlp_spam_proxy.md").exists())


if __name__ == "__main__":
    unittest.main()
