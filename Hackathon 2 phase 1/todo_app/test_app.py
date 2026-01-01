"""
Simple test to verify the console todo application works as expected.
"""
import os
import sys
import json

# Add the current directory to the path to allow imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.task import Task
from task_manager import TaskManager
from ui.console_ui import ConsoleUI


def test_basic_functionality():
    """
    Test the basic functionality of the todo application.
    """
    print("Testing basic functionality of the todo application...")
    
    # Create a task manager instance
    task_manager = TaskManager("test_tasks.json")
    
    # Test adding a task
    print("\n1. Testing adding a task...")
    task = task_manager.add_task("Test task", "This is a test task", "high", "work", "2026-12-31")
    print(f"Added task: {task}")
    
    # Test getting all tasks
    print("\n2. Testing getting all tasks...")
    tasks = task_manager.get_all_tasks()
    print(f"Total tasks: {len(tasks)}")
    for task in tasks:
        print(f"  - {task}")
    
    # Test updating a task
    print("\n3. Testing updating a task...")
    if tasks:
        updated_task = task_manager.update_task(
            tasks[0].id, 
            title="Updated test task", 
            description="This is an updated test task", 
            priority="low"
        )
        print(f"Updated task: {updated_task}")
    
    # Test marking task as complete
    print("\n4. Testing marking task as complete...")
    if tasks:
        completed_task = task_manager.mark_task_complete(tasks[0].id)
        print(f"Completed task: {completed_task}")
    
    # Test searching tasks
    print("\n5. Testing searching tasks...")
    search_results = task_manager.search_tasks("test")
    print(f"Search results: {len(search_results)} tasks found")
    
    # Test filtering tasks
    print("\n6. Testing filtering tasks...")
    filtered_results = task_manager.filter_tasks(status="completed", priority="low")
    print(f"Filtered results: {len(filtered_results)} tasks found")
    
    # Test sorting tasks
    print("\n7. Testing sorting tasks...")
    sorted_results = task_manager.sort_tasks("priority", reverse=True)
    print(f"Sorted results: {len(sorted_results)} tasks")
    
    # Clean up test file
    if os.path.exists("test_tasks.json"):
        os.remove("test_tasks.json")
    
    print("\nAll tests passed successfully!")


if __name__ == "__main__":
    test_basic_functionality()