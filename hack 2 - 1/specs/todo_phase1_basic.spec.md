# Specification: Phase I - Todo In-Memory Python Console Application

## 1. Objective

To create a simple, functional, console-based Todo application. This initial phase focuses on core CRUD (Create, Read, Update, Delete) operations for managing tasks. All data will be stored in-memory, meaning it will be lost when the application closes.

## 2. Scope (Basic Level)

This phase is strictly limited to the essential functionality required for a minimal viable product.

### In Scope:
- Adding a new task with a title and description.
- Viewing a list of all existing tasks.
- Updating an existing task's title or description.
- Deleting a task by its ID.
- Changing a task's status (e.g., from 'incomplete' to 'complete' and vice-versa).
- Interaction solely through a command-line interface (CLI).

### Out of Scope:
- Data persistence (no file or database storage).
- User authentication or multiple user accounts.
- Task categories, tags, or priorities.
- Due dates or reminders.
- Graphical User Interface (GUI) or web interface.
- Any form of networking or remote access.

## 3. Functional Requirements

### 3.1. Add Task
- The user must be able to add a new task.
- Each task must have a `title` and a `description`.
- Each new task is assigned a unique, sequential ID.
- By default, a new task has a status of "incomplete".

### 3.2. View All Tasks
- The user must be able to view all tasks in a clear, formatted list.
- Each task in the list must display its ID, status, title, and description.

### 3.3. Update Task
- The user must be able to update the `title` and/or `description` of an existing task by providing its ID.

### 3.4. Delete Task
- The user must be able to delete a task by providing its ID.
- The application should confirm the deletion or handle cases where the ID does not exist.

### 3.5. Mark Task Status
- The user must be able to change the status of a task by providing its ID.
- The user can mark a task as "complete".
- The user can mark a task as "incomplete".

## 4. Non-Functional Requirements

- **Performance:** The application should respond to user commands instantly.
- **Usability:** The command-line interface should be intuitive and provide clear instructions to the user.
- **Reliability:** The application should handle invalid user input gracefully (e.g., non-existent IDs, incorrect commands).
- **Modularity:** The code should be organized into logical, decoupled modules (e.g., one for business logic, one for the CLI).

## 5. Constraints

- **Language:** Python 3.13.
- **Environment:** Console only.
- **Data Storage:** In-memory only. The application state is ephemeral.
- **Dependencies:** No external libraries are to be used in Phase I. Only the Python standard library is permitted.

## 6. Acceptance Criteria

### 6.1. Add Task
- **Given** I run the application,
- **When** I select the "add task" command and provide a title "Buy Milk" and description "Get 2% milk from the store",
- **Then** a new task is created.
- **And** when I view all tasks, I see a task with ID 1, status "incomplete", title "Buy Milk", and description "Get 2% milk from the store".

### 6.2. View All Tasks
- **Given** I have added two tasks,
- **When** I select the "view all tasks" command,
- **Then** I see a formatted list containing both tasks with their respective IDs, statuses, titles, and descriptions.

### 6.3. Update Task
- **Given** a task with ID 1 and title "Buy Milk" exists,
- **When** I select the "update task" command for ID 1 and provide a new title "Buy Almond Milk",
- **Then** the task's title is updated.
- **And** when I view the task, its title is "Buy Almond Milk".

### 6.4. Delete Task
- **Given** a task with ID 1 exists,
- **When** I select the "delete task" command for ID 1,
- **Then** the task is removed from the application's memory.
- **And** when I view all tasks, the task with ID 1 is no longer listed.

### 6.5. Mark Task Status
- **Given** a task with ID 1 and status "incomplete" exists,
- **When** I select the "mark complete" command for ID 1,
- **Then** the task's status is updated to "complete".
- **And** when I view the task, its status is "complete".
- **When** I then select the "mark incomplete" command for ID 1,
- **Then** the task's status is updated back to "incomplete".
