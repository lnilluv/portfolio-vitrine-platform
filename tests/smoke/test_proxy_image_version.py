from pathlib import Path
import unittest


class ProxyImageVersionTest(unittest.TestCase):
    def test_proxy_uses_recent_traefik_release(self) -> None:
        compose = Path("docker-compose.base.yml").read_text(encoding="utf-8")
        self.assertIn("image: traefik:v3.3", compose)


if __name__ == "__main__":
    unittest.main()
