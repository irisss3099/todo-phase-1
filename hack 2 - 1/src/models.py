# src/models.py
import dataclasses
from typing import List

@dataclasses.dataclass
class Task:
    """Represents a single task."""
    id: int
    title: str
    description: str
    category: str = "General"
    status: str = "incomplete"
    surah: str | None = None
    priority: str | None = None  # High, Medium, Low

