from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ProjectCard:
    slug: str
    title: str
    runtime_mode: str
    stack: List[str]
    skills: List[str]
    business_problem: str
    live_url: str
    repo_url: str
