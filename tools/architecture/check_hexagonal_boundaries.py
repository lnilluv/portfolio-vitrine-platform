import ast
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "services" / "portfolio-api" / "src" / "portfolio_api"

FORBIDDEN: Dict[str, List[str]] = {
    "domain": ["portfolio_api.application", "portfolio_api.adapters", "portfolio_api.composition_root"],
    "application": ["portfolio_api.adapters", "portfolio_api.composition_root"],
    "adapters": ["portfolio_api.composition_root"],
}


def layer_for(path: Path) -> str:
    parts = path.parts
    for layer in ("domain", "application", "adapters", "composition_root"):
        if layer in parts:
            return layer
    return ""


def read_imports(path: Path) -> List[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    found: List[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for imported in node.names:
                found.append(imported.name)
        if isinstance(node, ast.ImportFrom):
            if node.module:
                found.append(node.module)
    return found


def main() -> int:
    violations: List[str] = []
    for path in TARGET.rglob("*.py"):
        current_layer = layer_for(path)
        if current_layer not in FORBIDDEN:
            continue

        imports = read_imports(path)
        disallowed = FORBIDDEN[current_layer]
        for imported in imports:
            for prefix in disallowed:
                if imported.startswith(prefix):
                    violations.append(f"{path.relative_to(ROOT)} imports forbidden module {imported}")

    if violations:
        print("Hexagonal boundary violations found:")
        for violation in violations:
            print(f"- {violation}")
        return 1

    print("Hexagonal boundaries check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
