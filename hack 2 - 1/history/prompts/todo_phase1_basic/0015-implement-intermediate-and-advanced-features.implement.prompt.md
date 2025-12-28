---
id: 0015
title: Implement Intermediate and Advanced Features
stage: implement
date: 2025-12-28
surface: agent
model: gemini-1.5-flash
feature: todo_phase1_basic
branch: main
user: N/A
command: |
  You are extending an existing In-Memory Todo Console Application
  from Basic Level to Intermediate and Advanced Levels.

  Objective:
  Enhance organization, usability, and intelligence of the CLI app
  while ensuring it runs cleanly in a terminal environment without errors.

  Critical Constraints:
  - Python 3.13
  - Console / CLI based only
  - In-memory storage only
  - No database, no files
  - No browser or GUI features
  - App must run safely in WSL / terminal
  - Do NOT break existing features
  - Maintain backward compatibility

  ------------------------------------------------
  INTERMEDIATE LEVEL FEATURES (Organization & Usability)
  ------------------------------------------------

  1. ⭐ Priorities
     - Allow user to assign priority:
         High / Medium / Low
     - Priority selection should be optional but validated
     - Display priority clearly in task table
     - Use color indicators if possible:
         High = Red
         Medium = Yellow
         Low = Green

  2. 🏷️ Tags / Categories
     - Allow assigning tags or labels:
         work, home, study, personal, etc.
     - Tags should be optional
     - Store tags as a list
     - Display tags cleanly in task list

  3. 🔍 Search & Filter
     Implement CLI-safe search and filtering:
     - Search tasks by keyword (title or description)
     - Filter by:
         - Status (completed / pending)
         - Priority (high / medium / low)
         - Task type (general, work, prayer, etc.)
     - Menu-driven (no free-form complex input)

  4. ↕️ Sort Tasks
     Allow user to sort tasks by:
     - Due date (if exists)
     - Priority
     - Alphabetically (title A–Z)
     Sorting must be stable and reversible

  ------------------------------------------------
  ADVANCED LEVEL FEATURES (Intelligent – CLI SAFE)
  ------------------------------------------------

  5. 🔁 Recurring Tasks
     - Allow tasks to be marked as recurring:
         daily / weekly / monthly
     - When a recurring task is completed:
         - Automatically create the next instance
         - Preserve title, description, priority, tags
     - Recurring logic must not affect non-recurring tasks

  6. ⏰ Due Dates & Time Reminders (CLI-SAFE)
     - Allow user to set:
         - Due date (YYYY-MM-DD)
         - Optional due time (HH:MM)
     - Validate date and time input
     - Display due date/time in task table

     Reminder behavior:
     - On each app loop, check:
         - Overdue tasks
         - Tasks due within next X minutes
     - Display bold, colored terminal alerts
     - NO browser notifications
     - NO background threads

  ------------------------------------------------
  PRAYER TASK SAFETY (MUST REMAIN INTACT)
  ------------------------------------------------

  - Prayer tasks remain a separate category
  - Surah logic remains unchanged
  - No priority, tags, or recurrence should auto-attach to prayer tasks
  - Prayer tasks must not mix with general task logic

  ------------------------------------------------
  CODE QUALITY & SAFETY
  ------------------------------------------------

  - Use clean, modular functions
  - Validate all user input
  - Prevent crashes from invalid date/time
  - Keep CLI output clean, readable, and well-spaced
  - No external libraries beyond Python standard library
  - Maintain evaluator-friendly structure

  ------------------------------------------------
  OUTPUT REQUIREMENTS
  ------------------------------------------------

  - Update existing source files safely
  - Add helper functions only if necessary
  - Return updated code with file paths
  - Ensure the app runs without errors in terminal
  - Do NOT include explanations unless necessary
labels: ["enhancement", "intermediate-features", "advanced-features", "todo-app"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- src/models.py
- src/task_manager.py
- src/cli.py
tests: null
---

## Prompt

(Full multi-line prompt from the user is included here)

## Response snapshot

(A summary of the multiple tool calls would be here)

## Outcome

- ✅ Impact: Implemented a comprehensive set of intermediate and advanced features, significantly enhancing the application's functionality and user experience.
- 🧪 Tests: No tests were run for this action.
- 📁 Files: Three files modified: src/models.py, src/task_manager.py, src/cli.py
- 🔁 Next prompts: The user may want to test the fully-featured application.
- 🧠 Reflection: This was a large, multi-step implementation that required careful planning and execution. The step-by-step approach of updating the model, then the business logic, and finally the CLI proved to be effective.

## Evaluation notes (flywheel)

- Failure modes observed: The initial attempt to replace the entire cli.py file at once failed due to the complexity of the changes. The subsequent step-by-step replacement of individual methods was successful.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
