"""
Main entry point for the Console-Based Todo Application.

This module initializes the application and runs the main loop.
"""
import sys
import os
# Add the current directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from task_manager import TaskManager
from ui.console_ui import ConsoleUI


def main():
    """
    Main function to run the console-based todo application.
    """
    print("Welcome to the Todo Application!")
    
    # Initialize the task manager and UI
    task_manager = TaskManager()
    ui = ConsoleUI(task_manager)
    
    # Load existing tasks if any
    task_manager.load_tasks()
    
    # Run the main application loop
    try:
        ui.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Todo Application!")


if __name__ == "__main__":
    main()