```python
---
id: 0009
title: Enhance CLI with Colors, Namaz Todos, and Cursor Navigation
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
  Make the CLI highly readable, elegant, and user-friendly while adding special Namaz Todos with Surahs.

  Constraints:
  - Python 3.13
  - In-memory storage only
  - Console-based (Windows)
  - Do NOT break existing functionality
  - Follow clean code & modular principles
  - Emojis allowed
  - Bold and colored messages allowed (use ANSI codes)
  - No database / file persistence
  - Each Namaz todo must be independent (complete one does not affect others)

  Enhancements Required:

  1. 🎨 CLI Readability & Styling
     - Clear headings and separators
     - Use spacing for readability
     - Use emojis where appropriate (📌 ✅ ⏳ 🕌)
     - Completed tasks should show [✔] in green, pending [⏳] in yellow
     - Important messages (task added, deleted, completed) should be bold and colored
     - Display should never look messy

  2. 🕌 Namaz Todos with Surahs
     - User can select “5-Time Prayers” todo type
     - Automatically create 5 todos:
         - Fajr 🕌 – Surah Yaseen
         - Dhuhr 🕌 – Surah Rahman
         - Asr 🕌 – Surah Manzil
         - Maghrib 🕌 – Surah Waqai
         - Isha 🕌 – Surah Mulk
     - Each Namaz has:
         - Its own status (complete / incomplete)
         - Its own Surah displayed below the task
         - Independent completion (marking one complete does not affect others)
     - Surah should always display even if task incomplete

  3. 🖱️ Cursor-Style Navigation
     - Implement simple cursor/number-based navigation for:
         - Selecting tasks
         - Marking complete / incomplete
         - Deleting tasks
     - Display current selection clearly
     - User can move up/down and select options by number

  4. 📋 General Todos
     - Retain existing General, Work, Personal todos
     - Each todo should have title, description, type
     - Completed tasks should be marked clearly
     - Use consistent styling for all tasks

  5. 🧼 Code Quality
     - Modular functions for:
         - Displaying tasks
         - Adding todos
         - Updating todos
         - Deleting todos
         - Marking complete/incomplete
     - Reuse existing logic
     - Avoid overengineering

  Output Requirements:
  - Update existing src/ files or create minimal new helper modules
  - Provide clean Python code with ANSI colors / emojis for styling
  - Include proper spacing and headings in CLI display
  - Ensure prayer todos display Surahs correctly
  - Cursor-style selection should be intuitive and clear
  - Return all files with their paths
  - Do NOT include extra explanations unless necessary
labels: ["enhancement", "ux", "cli", "colors", "namaz", "todo-app"]
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

You are enhancing an existing Phase I In-Memory Todo Console Application.

Objective:
Make the CLI highly readable, elegant, and user-friendly while adding special Namaz Todos with Surahs.

Constraints:
- Python 3.13
- In-memory storage only
- Console-based (Windows)
- Do NOT break existing functionality
- Follow clean code & modular principles
- Emojis allowed
- Bold and colored messages allowed (use ANSI codes)
- No database / file persistence
- Each Namaz todo must be independent (complete one does not affect others)

Enhancements Required:

1. 🎨 CLI Readability & Styling
   - Clear headings and separators
   - Use spacing for readability
   - Use emojis where appropriate (📌 ✅ ⏳ 🕌)
   - Completed tasks should show [✔] in green, pending [⏳] in yellow
   - Important messages (task added, deleted, completed) should be bold and colored
   - Display should never look messy

2. 🕌 Namaz Todos with Surahs
   - User can select “5-Time Prayers” todo type
   - Automatically create 5 todos:
       - Fajr 🕌 – Surah Yaseen
       - Dhuhr 🕌 – Surah Rahman
       - Asr 🕌 – Surah Manzil
       - Maghrib 🕌 – Surah Waqai
       - Isha 🕌 – Surah Mulk
   - Each Namaz has:
       - Its own status (complete / incomplete)
       - Its own Surah displayed below the task
       - Independent completion (marking one complete does not affect others)
   - Surah should always display even if task incomplete

3. 🖱️ Cursor-Style Navigation
   - Implement simple cursor/number-based navigation for:
       - Selecting tasks
       - Marking complete / incomplete
       - Deleting tasks
   - Display current selection clearly
   - User can move up/down and select options by number

4. 📋 General Todos
   - Retain existing General, Work, Personal todos
   - Each todo should have title, description, type
   - Completed tasks should be marked clearly
   - Use consistent styling for all tasks

5. 🧼 Code Quality
   - Modular functions for:
       - Displaying tasks
       - Adding todos
       - Updating todos
       - Deleting todos
       - Marking complete/incomplete
   - Reuse existing logic
   - Avoid overengineering

Output Requirements:
- Update existing src/ files or create minimal new helper modules
- Provide clean Python code with ANSI colors / emojis for styling
- Include proper spacing and headings in CLI display
- Ensure prayer todos display Surahs correctly
- Cursor-style selection should be intuitive and clear
- Return all files with their paths
- Do NOT include extra explanations unless necessary

## Response snapshot

Successfully modified file: C:\Users\MAK TECH\Desktop\coding at governer house\hack 2 - 1\src\models.py (1 replacements).
Successfully modified file: C:\Users\MAK TECH\Desktop\coding at governer house\hack 2 - 1\src\task_manager.py (1 replacements).
Successfully modified file: C:\Users\MAK TECH\Desktop\coding at governer house\hack 2 - 1\src\cli.py (1 replacements).

## Outcome

- ✅ Impact: Implemented significant CLI enhancements with colors, Namaz todos with Surahs, and cursor-style navigation.
- 🧪 Tests: No tests were run for this action.
- 📁 Files: Three files modified: src/models.py, src/task_manager.py, src/cli.py
- 🔁 Next prompts: User may want to run the application to see the changes.
- 🧠 Reflection: The application now has a much more user-friendly and feature-rich CLI. The code was refactored for better modularity.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A

```