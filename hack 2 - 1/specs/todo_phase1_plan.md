# Architectural Plan: Phase I - Todo In-Memory Python Console Application

This document outlines the architectural plan for the Todo application, covering the initial implementation and subsequent enhancements.

## 1. Scope and Dependencies

-   **In Scope:**
    -   Core task management features (CRUD operations).
    -   In-memory data storage (ephemeral).
    -   Console-based user interface.
    -   Task categorization, including a special "5-Time Prayers" category.
    -   Enhanced console aesthetics and user experience.
-   **Out of Scope:**
    -   Data persistence (file or database storage).
    -   User authentication and multi-user support.
    -   Web or GUI interfaces.
    -   Advanced features like due dates, reminders, or sub-tasks.
-   **External Dependencies:**
    -   Python 3.13 Standard Library only. No external packages are required.

## 2. Key Decisions and Rationale

-   **Decision: Modular Architecture**
    -   The application is structured into three main components: `models.py`, `task_manager.py`, and `cli.py`.
    -   **Rationale:** This separation of concerns improves maintainability, scalability, and testability.
        -   `models.py`: Defines the data structure (`Task` class), providing a single source of truth for the application's data model.
        -   `task_manager.py`: Encapsulates all business logic for task management, isolating it from the presentation layer.
        -   `cli.py`: Handles all user interaction, keeping the UI logic separate from the core application logic.
-   **Decision: In-Memory Data Storage**
    -   Tasks are stored in a simple Python list within the `TaskManager` instance.
    -   **Rationale:** This approach is simple, fast, and meets the Phase I requirement of no persistence. It simplifies the application by avoiding the complexity of database connections or file I/O.

## 3. Interfaces and API Contracts

The core application logic is exposed through the `TaskManager` class, which serves as the "API" for the CLI.

-   **`TaskManager` Public Interface:**
    -   `add_task(title: str, description: str, category: str) -> Task`: Creates and adds a new task.
    -   `view_tasks() -> List[Task]`: Retrieves all tasks.
    -   `update_task(task_id: int, title: str, description: str) -> Optional[Task]`: Updates an existing task.
    -   `delete_task(task_id: int) -> bool`: Deletes a task.
    -   `set_task_status(task_id: int, status: str) -> Optional[Task]`: Updates the status of a task.

## 4. Non-Functional Requirements (NFRs)

-   **Performance:** The application must be responsive, with all operations completing in under a second. In-memory operations ensure this is met.
-   **Usability:** The console interface is designed to be intuitive, with a clear menu, descriptive prompts, and emojis to enhance readability.
-   **Reliability:** The application handles invalid user input gracefully (e.g., non-numeric IDs, invalid menu choices) and provides clear error messages.
-   **Modularity:** The codebase is organized into logical modules, as described in the Key Decisions section.

## 5. Data Management

-   **Source of Truth:** The `_tasks` list within the `TaskManager` instance is the single source of truth for the application's state.
-   **Schema:** The `Task` dataclass in `models.py` defines the data schema.
-   **Data Lifetime:** All data is ephemeral and will be lost when the application is terminated.

## 6. Operational Readiness

-   **Deployment:** The application is run as a simple Python script.
-   **Running the Application:**
    1.  Ensure Python 3.13 is installed.
    2.  Navigate to the project's root directory.
    3.  Run the command: `python src/main.py`

## 7. Risk Analysis and Mitigation

-   **Risk 1: Data Loss**
    -   **Description:** All task data is lost upon application exit, as per the requirements.
    -   **Mitigation:** This is an accepted risk for Phase I. The user is implicitly aware of the in-memory nature of the application. For future phases, a persistence layer (e.g., SQLite, JSON file) could be introduced.
-   **Risk 2: Scalability**
    -   **Description:** Storing all tasks in a single list may become inefficient with a very large number of tasks.
    -   **Mitigation:** For the scope of a personal console-based todo app, this is a low risk. If performance were to degrade, data structures could be optimized (e.g., using dictionaries for faster lookups).

## 8. Evaluation and Validation

-   The application's functionality is validated against the acceptance criteria outlined in `specs/todo_phase1_basic.spec.md`.
-   Manual testing by running the application and testing each menu option is the primary method of validation for this phase.

## 9. Architectural Decision Record (ADR)

-   **Suggestion:** The decision to use a modular architecture (models, task_manager, cli) is a significant architectural choice. It is recommended to document this in an ADR for future reference.
