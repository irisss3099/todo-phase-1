---
id: 0014
title: Refine Task Categorization and Prayer Tasks
stage: implement
date: 2025-12-28
surface: agent
model: gemini-1.5-flash
feature: todo_phase1_basic
branch: main
user: N/A
command: |
  You are enhancing an existing Phase I In-Memory Todo Console Application.

  Objective:
  Refine task categorization logic and strictly separate Prayer (Namaz) tasks from all other task types.

  Constraints:
  - Python 3.13
  - Console-based only
  - In-memory storage only
  - No database or file persistence
  - Do NOT remove any existing mandatory Phase I features
  - Keep code clean, modular, and readable
  - Ensure backward compatibility

  Mandatory Phase I Features (must remain fully functional):
  1. Adding tasks with title and description
  2. Listing all tasks with status indicators
  3. Updating task details
  4. Deleting tasks by ID
  5. Marking tasks as complete / incomplete

  Enhancements Required:

  1. 🧾 Task Type Selection on Add Task
     When user adds a new task, prompt them to select a task type from:
     - General
     - Work
     - Personal
     - Hobby
     - Prayer (Namaz)

     Rules:
     - Task type selection is mandatory
     - Invalid input should be handled gracefully
     - Task type should be stored as part of the task object

  2. 🕌 Prayer (Namaz) Tasks – Strict Rules
     - Prayer tasks must ONLY exist under the "Prayer" category
     - No General / Work / Personal / Hobby task may contain Surah information
     - Surah field must exist ONLY for Prayer tasks

  3. 🕌 Prayer Tasks with Fixed Surahs
     When task type = "Prayer":
     Automatically assign Surah as follows:
     - Fajr → Surah Yaseen
     - Dhuhr → Surah Rahman
     - Asr → Surah Manzil
     - Maghrib → Surah Waqai
     - Isha → Surah Mulk

     Rules:
     - Each prayer is a separate task
     - Each prayer has its own completion status
     - Completing one prayer does NOT affect others
     - Surah must always be displayed with Prayer tasks
     - Surah must never appear for non-prayer tasks

  4. 📋 Task Display Rules
     - All tasks should display:
         ID | Title | Description | Type | Status
     - Prayer tasks should additionally display:
         Surah
     - Non-prayer tasks must NOT display any Surah column/value

  5. 🧼 Code Quality & Safety
     - Use clear conditional logic for Prayer vs Non-Prayer tasks
     - Avoid mixing prayer logic with general task logic
     - Reuse existing structures where possible
     - Keep UI clean and readable

  Output Requirements:
  - Update existing source files only where required
  - If a new helper function or enum is needed for task types, add it cleanly
  - Return updated code with file paths
  - Do NOT include explanations unless necessary
labels: ["refactor", "ux", "cli", "categorization", "prayer-tasks", "todo-app"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- src/cli.py
tests: null
---

## Prompt

You are enhancing an existing Phase I In-Memory Todo Console Application.

Objective:
Refine task categorization logic and strictly separate Prayer (Namaz) tasks from all other task types.

Constraints:
- Python 3.13
- Console-based only
- In-memory storage only
- No database or file persistence
- Do NOT remove any existing mandatory Phase I features
- Keep code clean, modular, and readable
- Ensure backward compatibility

Mandatory Phase I Features (must remain fully functional):
1. Adding tasks with title and description
2. Listing all tasks with status indicators
3. Updating task details
4. Deleting tasks by ID
5. Marking tasks as complete / incomplete

Enhancements Required:

1. 🧾 Task Type Selection on Add Task
   When user adds a new task, prompt them to select a task type from:
   - General
   - Work
   - Personal
   - Hobby
   - Prayer (Namaz)

   Rules:
   - Task type selection is mandatory
   - Invalid input should be handled gracefully
   - Task type should be stored as part of the task object

2. 🕌 Prayer (Namaz) Tasks – Strict Rules
   - Prayer tasks must ONLY exist under the "Prayer" category
   - No General / Work / Personal / Hobby task may contain Surah information
   - Surah field must exist ONLY for Prayer tasks

3. 🕌 Prayer Tasks with Fixed Surahs
   When task type = "Prayer":
   Automatically assign Surah as follows:
   - Fajr → Surah Yaseen
   - Dhuhr → Surah Rahman
   - Asr → Surah Manzil
   - Maghrib → Surah Waqai
   - Isha → Surah Mulk

   Rules:
   - Each prayer is a separate task
   - Each prayer has its own completion status
   - Completing one prayer does NOT affect others
   - Surah must always be displayed with Prayer tasks
   - Surah must never appear for non-prayer tasks

4. 📋 Task Display Rules
   - All tasks should display:
       ID | Title | Description | Type | Status
   - Prayer tasks should additionally display:
       Surah
   - Non-prayer tasks must NOT display any Surah column/value

5. 🧼 Code Quality & Safety
   - Use clear conditional logic for Prayer vs Non-Prayer tasks
   - Avoid mixing prayer logic with general task logic
   - Reuse existing structures where possible
   - Keep UI clean and readable

Output Requirements:
- Update existing source files only where required
- If a new helper function or enum is needed for task types, add it cleanly
- Return updated code with file paths
- Do NOT include explanations unless necessary

## Response snapshot

Successfully modified file: C:\Users\MAK TECH\Desktop\coding at governer house\hack 2 - 1\src\cli.py (1 replacements).

## Outcome

- ✅ Impact: Refactored the CLI to enforce stricter task categorization and a more robust and separate logic for handling Prayer (Namaz) tasks.
- 🧪 Tests: No tests were run for this action.
- 📁 Files: One file modified: src/cli.py
- 🔁 Next prompts: The user may want to test the updated application.
- 🧠 Reflection: The changes improve the application's data integrity by ensuring Prayer tasks are handled distinctly from other task types.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
