import json
from pathlib import Path
from typing import Any, Dict, List

from portfolio_api.domain.models import ProjectCard


class InMemoryProjectRepository:
    def __init__(self, source_path: Path | None = None) -> None:
        if source_path is None:
            source_path = self._discover_default_source_path()
        self._source_path = source_path

    def list_projects(self) -> List[ProjectCard]:
        rows = self._read_rows()
        return [
            ProjectCard(
                slug=row["slug"],
                title=row["title"],
                runtime_mode=row["runtime_mode"],
                stack=list(row.get("stack", [])),
                skills=list(row.get("skills", [])),
                business_problem=row["business_problem"],
                live_url=row["live_url"],
                repo_url=row["repo_url"],
            )
            for row in rows
        ]

    def _read_rows(self) -> List[Dict[str, Any]]:
        raw = json.loads(self._source_path.read_text(encoding="utf-8"))
        return list(raw or [])

    def _discover_default_source_path(self) -> Path:
        current = Path(__file__).resolve()
        for parent in current.parents:
            candidate = parent / "data" / "projects" / "projects.json"
            if candidate.exists():
                return candidate
        raise FileNotFoundError("Unable to locate data/projects/projects.json")
