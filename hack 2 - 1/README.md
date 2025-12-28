# Todo In-Memory Console Application

## Project Overview

This is a simple console-based Todo application developed in Python. It allows users to manage their tasks (add, view, update, delete, and mark status) directly from the command line. All task data is stored in memory and is not persisted, meaning tasks will be lost once the application is closed. This project serves as a foundational example of a spec-driven development process, focusing on clean architecture and adherence to defined specifications and constraints.

## Features

The application provides the following core functionalities:

1.  **Add Task**: Create a new task with a title and description. Tasks are automatically assigned a unique ID and initialized as "incomplete".
2.  **View All Tasks**: Display a formatted list of all existing tasks, including their ID, status, title, and description.
3.  **Update Task**: Modify the title and/or description of an existing task using its unique ID.
4.  **Delete Task**: Remove a task from the list using its unique ID.
5.  **Mark Task Status**: Change the status of a task to "complete" or "incomplete" using its unique ID.

## Tech Stack

-   **Language**: Python 3.13
-   **Dependencies**: Python Standard Library only (no external libraries)
-   **Environment**: Console-based application

## Setup using UV

This project uses `uv` for dependency management and environment setup. If you don't have `uv` installed, you can install it using `pipx`:

```bash
pipx install uv
```

Once `uv` is installed, set up the project environment:

```bash
uv venv
uv pip install -r requirements.txt # (Assuming requirements.txt will be created later if needed)
```

## How to Run

1.  **Activate the virtual environment**:
    ```bash
    .\.venv\Scripts\Activate.ps1 # On Windows (PowerShell)
    source ./.venv/bin/activate # On macOS/Linux
    ```
2.  **Navigate to the project root**:
    ```bash
    cd /path/to/your/project
    ```
3.  **Run the application**:
    ```bash
    python src/main.py
    ```

## Sample CLI Usage

Upon running the application, you will be presented with a menu. Enter the corresponding number to perform an action.

```
--- Todo Application ---
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task as Complete
6. Mark Task as Incomplete
7. Exit
------------------------
Enter your choice: 1
Enter task title: Buy Groceries
Enter task description: Milk, Eggs, Bread
Task 'Buy Groceries' added successfully with ID 1.

--- Todo Application ---
...
Enter your choice: 2
ID: 1, Status: incomplete, Title: Buy Groceries, Description: Milk, Eggs, Bread

--- Todo Application ---
...
Enter your choice: 5
Enter task ID to mark as complete: 1
Task 1 marked as complete.

--- Todo Application ---
...
Enter your choice: 2
ID: 1, Status: complete, Title: Buy Groceries, Description: Milk, Eggs, Bread

--- Todo Application ---
...
Enter your choice: 7
Exiting...
```
