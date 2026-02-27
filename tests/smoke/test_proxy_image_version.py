from pathlib import Path
import unittest


class ProxyImageVersionTest(unittest.TestCase):
    def test_proxy_sets_compatible_docker_api_version(self) -> None:
        compose = Path("docker-compose.base.yml").read_text(encoding="utf-8")
        self.assertIn("image: traefik:v3.3", compose)
        self.assertIn("DOCKER_API_VERSION: \"1.44\"", compose)


if __name__ == "__main__":
    unittest.main()
