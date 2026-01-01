"""
Console UI for the Console-Based Todo Application.

This module handles the console user interface for the application.
"""
from typing import List

from task_manager import TaskManager
from models.task import Task


class ConsoleUI:
    """
    Handles the console user interface for the todo application.
    """
    
    def __init__(self, task_manager: TaskManager):
        """
        Initialize the console UI with a task manager.
        
        Args:
            task_manager: The task manager instance to interact with
        """
        self.task_manager = task_manager
    
    def display_menu(self):
        """
        Display the main menu options to the user.
        """
        print("\n" + "="*50)
        print("Todo Application")
        print("="*50)
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as complete")
        print("6. Mark task as pending")
        print("7. Search tasks")
        print("8. Filter tasks")
        print("9. Sort tasks")
        print("0. Exit")
        print("-"*50)
    
    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.
        
        Returns:
            The user's menu choice as a string
        """
        choice = input("Enter your choice (0-9): ").strip()
        return choice
    
    def display_tasks(self, tasks: List[Task]):
        """
        Display a list of tasks to the user.
        
        Args:
            tasks: A list of Task objects to display
        """
        if not tasks:
            print("\nNo tasks found.")
            return
        
        print(f"\nFound {len(tasks)} task(s):")
        print("-" * 60)
        for task in tasks:
            print(f"  {task}")
            if task.description:
                print(f"      Description: {task.description}")
            if task.due_date:
                print(f"      Due Date: {task.due_date}")
            if task.category:
                print(f"      Category: {task.category}")
            print()
    
    def add_task_ui(self):
        """
        Handle the UI flow for adding a new task.
        """
        print("\nAdding a new task:")
        title = input("Enter task title: ").strip()
        
        if not title:
            print("Error: Task title cannot be empty.")
            return
        
        description = input("Enter task description (optional): ").strip()
        description = description if description else None
        
        print("Select priority (1: High, 2: Medium, 3: Low): ", end="")
        priority_choice = input().strip()
        priority_map = {"1": "high", "2": "medium", "3": "low"}
        priority = priority_map.get(priority_choice, "medium")
        
        category = input("Enter task category (optional): ").strip()
        category = category if category else None
        
        due_date = input("Enter due date (YYYY-MM-DD, optional): ").strip()
        due_date = due_date if due_date else None
        
        try:
            task = self.task_manager.add_task(title, description, priority, category, due_date)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error adding task: {e}")
    
    def update_task_ui(self):
        """
        Handle the UI flow for updating a task.
        """
        print("\nUpdating a task:")
        try:
            task_id = int(input("Enter task ID to update: ").strip())
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        # Check if task exists
        task = self.task_manager.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        print(f"Current task: {task}")
        if task.description:
            print(f"  Description: {task.description}")
        if task.due_date:
            print(f"  Due Date: {task.due_date}")
        if task.category:
            print(f"  Category: {task.category}")
        
        print("\nEnter new values (press Enter to keep current value):")
        new_title = input(f"Title (current: {task.title}): ").strip()
        new_title = new_title if new_title else task.title
        
        new_description = input(f"Description (current: {task.description or ''}): ").strip()
        new_description = new_description if new_description else task.description
        
        print(f"Priority (current: {task.priority}) - Select (1: High, 2: Medium, 3: Low, Enter: keep current): ", end="")
        priority_choice = input().strip()
        priority_map = {"1": "high", "2": "medium", "3": "low"}
        new_priority = priority_map.get(priority_choice, task.priority if not priority_choice else task.priority)
        
        new_category = input(f"Category (current: {task.category or ''}): ").strip()
        new_category = new_category if new_category else task.category
        
        new_due_date = input(f"Due date (current: {task.due_date or ''}, format: YYYY-MM-DD): ").strip()
        new_due_date = new_due_date if new_due_date else task.due_date
        
        try:
            updated_task = self.task_manager.update_task(
                task_id, new_title, new_description, new_priority, new_category, new_due_date
            )
            print(f"Task updated successfully: {updated_task}")
        except ValueError as e:
            print(f"Error updating task: {e}")
    
    def delete_task_ui(self):
        """
        Handle the UI flow for deleting a task.
        """
        print("\nDeleting a task:")
        try:
            task_id = int(input("Enter task ID to delete: ").strip())
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        task = self.task_manager.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        print(f"Task to delete: {task}")
        confirm = input("Are you sure you want to delete this task? (y/N): ").strip().lower()
        
        if confirm in ['y', 'yes']:
            try:
                self.task_manager.delete_task(task_id)
                print("Task deleted successfully.")
            except ValueError as e:
                print(f"Error deleting task: {e}")
        else:
            print("Task deletion cancelled.")
    
    def mark_task_complete_ui(self):
        """
        Handle the UI flow for marking a task as complete.
        """
        print("\nMarking task as complete:")
        try:
            task_id = int(input("Enter task ID to mark as complete: ").strip())
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        task = self.task_manager.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        try:
            updated_task = self.task_manager.mark_task_complete(task_id)
            print(f"Task marked as complete: {updated_task}")
        except ValueError as e:
            print(f"Error marking task as complete: {e}")
    
    def mark_task_pending_ui(self):
        """
        Handle the UI flow for marking a task as pending.
        """
        print("\nMarking task as pending:")
        try:
            task_id = int(input("Enter task ID to mark as pending: ").strip())
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            return
        
        task = self.task_manager.get_task_by_id(task_id)
        if not task:
            print(f"Error: Task with ID {task_id} not found.")
            return
        
        try:
            updated_task = self.task_manager.mark_task_pending(task_id)
            print(f"Task marked as pending: {updated_task}")
        except ValueError as e:
            print(f"Error marking task as pending: {e}")
    
    def search_tasks_ui(self):
        """
        Handle the UI flow for searching tasks.
        """
        print("\nSearching tasks:")
        search_term = input("Enter search term: ").strip()
        
        if not search_term:
            print("Error: Search term cannot be empty.")
            return
        
        tasks = self.task_manager.search_tasks(search_term)
        self.display_tasks(tasks)
    
    def filter_tasks_ui(self):
        """
        Handle the UI flow for filtering tasks.
        """
        print("\nFiltering tasks:")
        print("Filter by status (1: Pending, 2: Completed, Enter: no filter): ", end="")
        status_choice = input().strip()
        status_map = {"1": "pending", "2": "completed"}
        status = status_map.get(status_choice)
        
        print("Filter by priority (1: High, 2: Medium, 3: Low, Enter: no filter): ", end="")
        priority_choice = input().strip()
        priority_map = {"1": "high", "2": "medium", "3": "low"}
        priority = priority_map.get(priority_choice)
        
        category = input("Filter by category (optional): ").strip()
        category = category if category else None
        
        tasks = self.task_manager.filter_tasks(status, priority, category)
        self.display_tasks(tasks)
    
    def sort_tasks_ui(self):
        """
        Handle the UI flow for sorting tasks.
        """
        print("\nSorting tasks:")
        print("Sort by (1: Priority, 2: Due Date, 3: Title, 4: Creation Date): ", end="")
        sort_choice = input().strip()
        sort_map = {"1": "priority", "2": "due_date", "3": "title", "4": "created_date"}
        sort_by = sort_map.get(sort_choice, "created_date")
        
        print("Order (1: Ascending, 2: Descending, default: Descending): ", end="")
        order_choice = input().strip()
        reverse = False if order_choice == "1" else True
        
        tasks = self.task_manager.sort_tasks(sort_by, reverse)
        self.display_tasks(tasks)
    
    def run(self):
        """
        Run the main application loop.
        """
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == "1":
                tasks = self.task_manager.get_all_tasks()
                self.display_tasks(tasks)
            elif choice == "2":
                self.add_task_ui()
            elif choice == "3":
                self.update_task_ui()
            elif choice == "4":
                self.delete_task_ui()
            elif choice == "5":
                self.mark_task_complete_ui()
            elif choice == "6":
                self.mark_task_pending_ui()
            elif choice == "7":
                self.search_tasks_ui()
            elif choice == "8":
                self.filter_tasks_ui()
            elif choice == "9":
                self.sort_tasks_ui()
            elif choice == "0":
                print("Saving tasks and exiting...")
                self.task_manager.save_tasks()
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 9.")
            
            # Pause to let user see the result
            input("\nPress Enter to continue...")