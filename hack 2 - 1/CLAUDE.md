# CLAUDE.md: A Guide to AI-Driven Development

## 1. Introduction

This document certifies that the **Phase I Todo In-Memory Python Console Application** was implemented entirely by **Claude Code**, an AI agent. No manual coding was involved in the creation, enhancement, or documentation of this project.

The purpose of this file is to document the development process, outline the project's architecture, and provide a clear guide for evaluators and future developers on how to interact with, run, and update the application using the same AI-driven, spec-first methodology.

## 2. The Agentic Dev Stack Workflow

Development followed a strict, repeatable workflow known as the **Agentic Dev Stack**. This process ensures that all development is deliberate, traceable, and aligned with pre-defined requirements.

The workflow consists of four distinct stages:

1.  **Spec (Specification):** The user provides a detailed specification for a feature or the entire application. This serves as the single source of truth for all requirements.
2.  **Plan (Architectural Plan):** The AI agent analyzes the specification and produces a high-level architectural plan, outlining key decisions, structure, and interfaces.
3.  **Tasks (Task Breakdown):** The plan is broken down into small, atomic, and testable development tasks, each designed for AI execution.
4.  **Implementation:** The AI agent executes each task sequentially, generating, and modifying the code until all requirements are met.

Every step of this process, including this `CLAUDE.md` file, is recorded in a `history/` directory for full transparency and auditability.

## 3. Core Features Implemented

This application was built to include all mandatory features for a Phase I in-memory todo application:

-   **Add Task:** Users can add a new task with a title and a detailed description. Tasks can be categorized into `General`, `Work`, `Personal`, or the special `5-Time Prayers` type.
-   **View All Tasks:** All tasks are displayed in a formatted, readable list, grouped by category and status.
-   **Update Task:** Existing task details can be modified.
-   **Delete Task:** Tasks can be removed from the list by selecting them via a cursor-style menu.
-   **Mark Status:** The status of any task can be toggled between `complete` and `incomplete`.
-   **Namaz Todos with Surahs:** A special feature that automatically generates the five daily prayer tasks, each with its designated Surah to recite.
-   **Enhanced CLI:** The console interface is styled with colors and emojis for readability and includes user-friendly navigation.

## 4. Architectural & Development Overview

-   **Folder Structure:**
    -   `src/`: Contains all application source code, organized into modules for models (`models.py`), business logic (`task_manager.py`), and the command-line interface (`cli.py`).
    -   `specs/`: Holds all specification, planning, and task-breakdown documents (`constitution.md`, `spec.md`, `plan.md`, `tasks.md`).
    -   `history/`: Contains a complete, timestamped log of every prompt and action taken by the AI agent.

-   **Technology Stack:**
    -   **Language:** Python 3.13+
    -   **Data Storage:** In-memory only. No databases or file persistence are used. All data is ephemeral.
    -   **Interface:** Console-based, designed for a standard Windows terminal.

-   **Spec-Driven Code Generation:**
    The entire application was generated based on the markdown documents in the `specs/` folder. The AI agent first established a `constitution.md` to define project rules, then followed the `spec.md`, `plan.md`, and `tasks.md` to implement the required functionality.

## 5. Instructions for Future Use

### Running the Application

To run the application, follow these steps from the project's root directory:

1.  Ensure Python 3.13 or newer is installed.
2.  Open a terminal or command prompt.
3.  Execute the following command:
    ```bash
    python src/main.py
    ```

### Updating the App with Claude Code

This project is designed to be maintained and updated exclusively by the Claude Code agent. To request a new feature or a change, follow the established workflow:

1.  **Create a New Spec:** Write a new `.spec.md` file detailing the new requirements. Be as clear and specific as possible.
2.  **Instruct the Agent:** Provide a prompt to the agent instructing it to read the new spec and implement the changes.
3.  **Review and Approve:** The agent will generate a plan and a task list for your approval before writing any code.

This `CLAUDE.md` file serves as a foundational reference for all future AI-driven interactions with the project.