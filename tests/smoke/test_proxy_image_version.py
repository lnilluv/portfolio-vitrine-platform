from pathlib import Path
import unittest


class ProxyImageVersionTest(unittest.TestCase):
    def test_proxy_uses_traefik_v34_or_newer(self) -> None:
        compose = Path("docker-compose.base.yml").read_text(encoding="utf-8")
        self.assertIn("image: traefik:v3.4", compose)


if __name__ == "__main__":
    unittest.main()
