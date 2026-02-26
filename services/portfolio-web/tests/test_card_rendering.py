from pathlib import Path
import unittest


class CardRenderingTest(unittest.TestCase):
    def test_web_assets_exist(self) -> None:
        self.assertTrue(Path("services/portfolio-web/index.html").exists())
        self.assertTrue(Path("services/portfolio-web/assets/app.js").exists())
        self.assertTrue(Path("services/portfolio-web/assets/styles.css").exists())


if __name__ == "__main__":
    unittest.main()
