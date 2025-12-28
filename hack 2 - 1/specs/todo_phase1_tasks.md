# Development Tasks: Phase I - Todo Application

Based on the specification `specs/todo_phase1_basic.spec.md`, the following atomic development tasks have been defined for AI execution.

**Feature:** `todo_phase1_basic`

---

### Task 1: Define the Core Task Model

-   **Title:** Create Task Data Class
-   **Details:** In a new file `main.py`, define a Python data class or a simple class named `Task` to represent a single todo item. The class must include the following attributes with type hints:
    -   `id`: `int`
    -   `title`: `str`
    -   `description`: `str`
    -   `status`: `str` (e.g., "incomplete", "complete")
-   **Related Requirement:** All functional requirements depending on the Task model.

---

### Task 2: Implement the Task Management Logic

-   **Title:** Create TaskManager Class
-   **Details:** In `main.py`, create a `TaskManager` class to handle the business logic for managing tasks. It should contain:
    -   An in-memory list to store `Task` objects.
    -   A counter for generating unique task IDs.
    -   An `add_task(title: str, description: str) -> Task` method that creates a new task, assigns it a unique ID, sets its default status to "incomplete", adds it to the list, and returns the newly created task.
-   **Related Requirement:** 3.1. Add Task

---

### Task 3: Implement Task Viewing Logic

-   **Title:** Implement `view_tasks` Method
-   **Details:** In the `TaskManager` class within `main.py`, add a method `view_tasks() -> list[Task]` that returns the complete list of tasks currently in memory.
-   **Related Requirement:** 3.2. View All Tasks

---

### Task 4: Implement Task Update Logic

-   **Title:** Implement `update_task` Method
-   **Details:** In the `TaskManager` class, add a method `update_task(task_id: int, title: str, description: str) -> Task | None` that finds a task by its ID and updates its title and description. It should return the updated task or `None` if the task ID is not found.
-   **Related Requirement:** 3.3. Update Task

---

### Task 5: Implement Task Deletion Logic

-   **Title:** Implement `delete_task` Method
-   **Details:** In the `TaskManager` class, add a method `delete_task(task_id: int) -> bool` that removes a task from the list by its ID. It should return `True` if deletion was successful and `False` if the task ID was not found.
-   **Related Requirement:** 3.4. Delete Task

---

### Task 6: Implement Task Status Logic

-   **Title:** Implement `set_task_status` Method
-   **Details:** In the `TaskManager` class, add a method `set_task_status(task_id: int, status: str) -> Task | None` that finds a task by its ID and updates its status. It should return the updated task or `None` if the task ID is not found.
-   **Related Requirement:** 3.5. Mark Task Status

---

### Task 7: Build the Basic Command-Line Interface (CLI)

-   **Title:** Create Initial CLI structure
-   **Details:** In `main.py`, create a `main()` function that will serve as the main application loop. This function should:
    -   Instantiate the `TaskManager`.
    -   Continuously prompt the user for a command (e.g., "add", "view", "exit").
    -   Include a simple `if/elif/else` structure to parse user commands.
    -   Handle an "exit" command to terminate the application.
-   **Related Requirement:** All (CLI interaction)

---

### Task 8: Integrate 'View All Tasks' into CLI

-   **Title:** Connect `view_tasks` to CLI
-   **Details:** In the `main()` function's loop, implement the "view" command. When the user enters "view", the application should call the `task_manager.view_tasks()` method and print the details of each task to the console in a user-friendly format.
-   **Related Requirement:** 3.2. View All Tasks

---

### Task 9: Integrate 'Add Task' into CLI

-   **Title:** Connect `add_task` to CLI
-   **Details:** In the `main()` function's loop, implement the "add" command. The application should prompt the user for a title and description, then call the `task_manager.add_task()` method with the provided inputs, and finally print a confirmation message.
-   **Related Requirement:** 3.1. Add Task

---

### Task 10: Integrate 'Update Task' into CLI

-   **Title:** Connect `update_task` to CLI
-   **Details:** In the `main()` function's loop, implement the "update" command. The application should prompt for a task ID, a new title, and a new description, and then call the `task_manager.update_task()` method. It should print a success or failure message.
-   **Related Requirement:** 3.3. Update Task

---

### Task 11: Integrate 'Delete Task' into CLI

-   **Title:** Connect `delete_task` to CLI
-   **Details:** In the `main()` function's loop, implement the "delete" command. The application should prompt the user for a task ID and call `task_manager.delete_task()`. It should then print a success or failure message.
-   **Related Requirement:** 3.4. Delete Task

---

### Task 12: Integrate 'Mark Task Status' into CLI

-   **Title:** Connect `set_task_status` to CLI
-   **Details:** In the `main()` function's loop, implement "complete" and "incomplete" commands. The app should prompt for a task ID and call `task_manager.set_task_status()` with the appropriate status. It should then print a success or failure message.
-   **Related Requirement:** 3.5. Mark Task Status
