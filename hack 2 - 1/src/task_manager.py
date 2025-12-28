# src/task_manager.py
from typing import List, Optional
from src.models import Task

class TaskManager:
    """Manages all the tasks."""

    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id = 1

    def add_task(self, title: str, description: str, category: str, surah: str | None = None,
                 priority: str | None = None) -> Task:
        """Adds a new task."""
        task = Task(id=self._next_id, title=title, description=description, category=category, surah=surah,
                    priority=priority)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Gets a task by its ID."""
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def get_tasks(self, search_keyword: str | None = None, filter_by_status: str | None = None,
                  filter_by_priority: str | None = None, filter_by_type: str | None = None,
                  sort_by: str | None = None, sort_reverse: bool = False) -> List[Task]:
        """Gets tasks with optional searching, filtering, and sorting."""
        tasks_to_return = self._tasks[:]

        # Search
        if search_keyword:
            tasks_to_return = [t for t in tasks_to_return if search_keyword.lower() in t.title.lower() or search_keyword.lower() in t.description.lower()]

        # Filter
        if filter_by_status:
            tasks_to_return = [t for t in tasks_to_return if t.status == filter_by_status]
        if filter_by_priority:
            tasks_to_return = [t for t in tasks_to_return if t.priority == filter_by_priority]
        if filter_by_type:
            tasks_to_return = [t for t in tasks_to_return if t.category == filter_by_type]
            
        # Sort
        if sort_by:
            if sort_by == 'priority':
                priority_map = {'High': 3, 'Medium': 2, 'Low': 1, None: 0}
                tasks_to_return.sort(key=lambda t: priority_map.get(t.priority, 0), reverse=not sort_reverse)
            elif sort_by == 'title':
                tasks_to_return.sort(key=lambda t: t.title.lower(), reverse=sort_reverse)

        return tasks_to_return

    def update_task(self, task_id: int, title: str, description: str) -> Optional[Task]:
        """Updates a task's title and description."""
        task = self.get_task_by_id(task_id)
        if task:
            task.title = title
            task.description = description
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        """Deletes a task by its ID."""
        task = self.get_task_by_id(task_id)
        if task:
            self._tasks.remove(task)
            return True
        return False

    def set_task_status(self, task_id: int, status: str) -> Optional[Task]:
        """Sets a task's status."""
        if status not in ["complete", "incomplete"]:
            return None
        task = self.get_task_by_id(task_id)
        if task:
            task.status = status
            return task
        return None
