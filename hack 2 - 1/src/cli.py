import os
import atexit
from src.task_manager import TaskManager
from typing import List
from src.models import Task

class Colors:
    """ANSI color codes for styling the console output."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GRAY = '\033[90m'

class CLI:
    """Command-Line Interface for the Todo App."""

    def __init__(self):
        self.task_manager = TaskManager()
        self.current_tasks_view = []
        # Register the exit message function to be called on program termination
        atexit.register(self._display_exit_message)

    def _display_welcome_banner(self):
        """Displays the welcome banner at the start of the application."""
        print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*50}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.HEADER}📝 Welcome to Todo App 📝{Colors.ENDC}")
        print(f"   Manage your tasks efficiently!")
        print(f"{Colors.BOLD}{Colors.HEADER}{'='*50}{Colors.ENDC}")

    def _display_exit_message(self):
        """Displays a clean exit message when the user quits the application."""
        print(f"\n{Colors.BOLD}{Colors.BLUE}🙏 Thank you for using Todo App!{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.BLUE}👋 Goodbye! 😊{Colors.ENDC}")

    def _display_menu(self):
        """Displays the main application menu with options."""
        print("\n" + Colors.BOLD + Colors.CYAN + "--- MAIN MENU ---" + Colors.ENDC)
        print("  1. 📋 View Tasks")
        print("  2. 📌 Add a New Task")
        print("  3. 🔍 Search, Filter & Sort Tasks")
        print("  4. ✏️ Update Task Details")
        print("  5. ❌ Delete Task by ID")
        print("  6. ✅ Mark Task Status")
        print("  7. 🚪 Exit")
        print(Colors.CYAN + "-----------------" + Colors.ENDC)

    def _display_tasks_table(self, tasks: List[Task]):
        """Displays a list of tasks in a formatted table."""
        if not tasks:
            print("\n" + Colors.YELLOW + "📋 No tasks found for the current view." + Colors.ENDC)
            return

        has_prayer_tasks = any(task.category == "Prayer" for task in tasks)

        header = f"{Colors.BOLD}{'ID':<5} | {'Task Title':<20} | {'Description':<30} | {'Priority':<15} | {'Status':<25}"
        if has_prayer_tasks:
            header += f" | {'Surah':<15}"
        header += Colors.ENDC
        
        table_width = 130 if has_prayer_tasks else 115

        print("\n" + Colors.BOLD + Colors.CYAN + "-"*table_width + Colors.ENDC)
        print(header)
        print(Colors.BOLD + Colors.CYAN + "-"*table_width + Colors.ENDC)

        priority_colors = {'High': Colors.RED, 'Medium': Colors.YELLOW, 'Low': Colors.GREEN}

        for task in tasks:
            status_indicator = f"{Colors.GREEN}[✔] Completed{Colors.ENDC}" if task.status == 'complete' else f"{Colors.YELLOW}[⏳] Pending{Colors.ENDC}"
            priority = f"{priority_colors.get(task.priority, '')}{task.priority if task.priority else ''}{Colors.ENDC}"
            
            title_display = (task.title[:17] + '...') if len(task.title) > 20 else task.title
            description_display = (task.description[:27] + '...') if len(task.description) > 30 else task.description

            row = f"{task.id:<5} | {title_display:<20} | {description_display:<30} | {priority:<25} | {status_indicator:<34}"
            if has_prayer_tasks:
                surah = task.surah if task.surah else ""
                row += f" | {surah:<15}"
            
            print(row)
        
        print(Colors.BOLD + Colors.CYAN + "-"*table_width + Colors.ENDC)

    def run(self):
        """Runs the main CLI loop."""
        if os.name == 'nt':
            os.system('')
        
        # 1. Welcome banner is called once at the start.
        self._display_welcome_banner() 

        while True:
            self._display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.current_tasks_view = self.task_manager.get_tasks()
                self._display_tasks_table(self.current_tasks_view)
            elif choice == '2':
                self._add_task()
            elif choice == '3':
                self._search_filter_sort_menu()
            elif choice == '4':
                self._update_task_by_id()
            elif choice == '5':
                self._delete_task_by_id()
            elif choice == '6':
                self._mark_task_status_by_id()
            elif choice == '7':
                # 2. The loop breaks, and atexit handles the exit message.
                break
            else:
                print(Colors.RED + "❌ Invalid choice." + Colors.ENDC)

    def _add_task(self):
        print("\n" + Colors.BOLD + Colors.CYAN + "--- 📌 ADD A NEW TASK ---" + Colors.ENDC)
        print("Select a task type:")
        print("  1. General, 2. Work, 3. Personal, 4. Hobby, 5. Prayer (Namaz)")
        type_choice = input("Enter choice: ")
        
        task_types = {"1": "General", "2": "Work", "3": "Personal", "4": "Hobby"}

        if type_choice == "5":
            self._add_prayer_task()
            return
        
        category = task_types.get(type_choice, "General")

        title = input("Enter task title: ")
        description = input("Enter task description: ")

        priority = None
        priority_choice = input("Enter priority (1. High, 2. Medium, 3. Low, Enter to skip): ")
        priorities = {"1": "High", "2": "Medium", "3": "Low"}
        if priority_choice in priorities:
            priority = priorities[priority_choice]

        self.task_manager.add_task(title, description, category, priority=priority)
        print(Colors.BOLD + Colors.GREEN + f"✅ Task '{title}' added successfully." + Colors.ENDC)

    def _add_prayer_task(self):
        print("\n" + Colors.BOLD + Colors.CYAN + "--- 🕌 ADD PRAYER TASK ---" + Colors.ENDC)
        print("Select a prayer:")
        print("  1. Fajr, 2. Dhuhr, 3. Asr, 4. Maghrib, 5. Isha")
        prayer_choice = input("Enter choice: ")

        prayers = {
            "1": ("Fajr", "Surah Yaseen"),
            "2": ("Dhuhr", "Surah Rahman"),
            "3": ("Asr", "Surah Manzil"),
            "4": ("Maghrib", "Surah Waqai"),
            "5": ("Isha", "Surah Mulk")
        }

        if prayer_choice in prayers:
            title, surah = prayers[prayer_choice]
            self.task_manager.add_task(title, f"Recite {surah}", "Prayer", surah=surah)
            print(Colors.BOLD + Colors.GREEN + f"✅ Prayer task '{title}' added." + Colors.ENDC)
        else:
            print(Colors.RED + "❌ Invalid prayer choice." + Colors.ENDC)

    def _search_filter_sort_menu(self):
        print("\n" + Colors.BOLD + Colors.CYAN + "--- 🔍 SEARCH, FILTER & SORT ---" + Colors.ENDC)
        print("  1. Search by Keyword")
        print("  2. Filter by Status")
        print("  3. Filter by Priority")
        print("  4. Filter by Type")
        print("  5. Sort Tasks")
        print("  6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            keyword = input("Enter keyword to search for: ")
            self.current_tasks_view = self.task_manager.get_tasks(search_keyword=keyword)
        elif choice == '2':
            status = input("Filter by status (complete/pending): ").lower()
            self.current_tasks_view = self.task_manager.get_tasks(filter_by_status=status)
        elif choice == '3':
            priority = input("Filter by priority (High/Medium/Low): ").capitalize()
            self.current_tasks_view = self.task_manager.get_tasks(filter_by_priority=priority)
        elif choice == '4':
            type = input("Filter by type (General, Work, etc.): ").capitalize()
            self.current_tasks_view = self.task_manager.get_tasks(filter_by_type=type)
        elif choice == '5':
            sort_by = input("Sort by (priority/title): ").lower()
            if sort_by not in ['priority', 'title']:
                print(Colors.RED + "❌ Invalid sort option." + Colors.ENDC)
                return
            reverse = input("Sort descending? (yes/no): ").lower() == 'yes'
            self.current_tasks_view = self.task_manager.get_tasks(sort_by=sort_by, sort_reverse=reverse)
        elif choice == '6':
            return
        else:
            print(Colors.RED + "❌ Invalid choice." + Colors.ENDC)
            return
        
        self._display_tasks_table(self.current_tasks_view)

    def _update_task_by_id(self):
        print("\n" + Colors.BOLD + Colors.CYAN + "--- ✏️ UPDATE TASK DETAILS ---" + Colors.ENDC)
        try:
            task_id = int(input("Enter the ID of the task to update: "))
            task = self.task_manager.get_task_by_id(task_id)
            if not task:
                print(Colors.RED + f"❌ Task with ID {task_id} not found." + Colors.ENDC)
                return
            
            title = input(f"Enter new title (current: {task.title}): ")
            description = input(f"Enter new description (current: {task.description}): ")
            
            if self.task_manager.update_task(task_id, title, description):
                print(Colors.BOLD + Colors.GREEN + f"✅ Task {task_id} updated successfully." + Colors.ENDC)
        except ValueError:
            print(Colors.RED + "❌ Invalid ID. Please enter a number." + Colors.ENDC)

    def _delete_task_by_id(self):
        print("\n" + Colors.BOLD + Colors.CYAN + "--- ❌ DELETE TASK BY ID ---" + Colors.ENDC)
        try:
            task_id = int(input("Enter the ID of the task to delete: "))
            task = self.task_manager.get_task_by_id(task_id)
            if not task:
                print(Colors.RED + f"❌ Task with ID {task_id} not found." + Colors.ENDC)
                return

            confirmation = input(f"Are you sure you want to delete '{task.title}'? (yes/no): ").lower()
            if confirmation == 'yes':
                if self.task_manager.delete_task(task_id):
                    print(Colors.BOLD + Colors.GREEN + f"✅ Task '{task.title}' deleted successfully." + Colors.ENDC)
            else:
                print("Deletion cancelled.")
        except ValueError:
            print(Colors.RED + "❌ Invalid ID. Please enter a number." + Colors.ENDC)

    def _mark_task_status_by_id(self):
        print("\n" + Colors.BOLD + Colors.CYAN + "--- ✅ MARK TASK STATUS ---" + Colors.ENDC)
        try:
            task_id = int(input("Enter the ID of the task to update: "))
            task = self.task_manager.get_task_by_id(task_id)
            if not task:
                print(Colors.RED + f"❌ Task with ID {task_id} not found." + Colors.ENDC)
                return

            status_choice = input(f"Mark '{task.title}' as (1) Complete or (2) Incomplete? Enter 1 or 2: ")
            if status_choice not in ['1', '2']:
                print(Colors.RED + "❌ Invalid choice." + Colors.ENDC)
                return
            
            status = "complete" if status_choice == '1' else "incomplete"
            if self.task_manager.set_task_status(task_id, status):
                print(Colors.BOLD + Colors.GREEN + f"✅ Task {task_id} status updated to {status}." + Colors.ENDC)
        except ValueError:
            print(Colors.RED + "❌ Invalid ID. Please enter a number." + Colors.ENDC)