"""
Task manager for the Console-Based Todo Application.

This module handles the core task management functionality.
"""
from typing import List, Optional, Dict, Any

from models.task import Task
from persistence.file_handler import FileHandler
from utils.validators import (
    validate_task_title,
    validate_task_status,
    validate_task_priority,
    validate_task_category,
    validate_task_due_date,
    validate_task_recurring
)


class TaskManager:
    """
    Manages tasks in the todo application.
    """
    
    def __init__(self, file_path: str = "tasks.json"):
        """
        Initialize the task manager with a file handler.
        
        Args:
            file_path: Path to the JSON file for task storage (default: "tasks.json")
        """
        self.file_handler = FileHandler(file_path)
        self.tasks: List[Task] = []
        self.next_task_id = 1
    
    def load_tasks(self):
        """
        Load tasks from the file.
        """
        self.tasks = self.file_handler.load_tasks()
        # Update the next_task_id based on the highest ID in the loaded tasks
        if self.tasks:
            self.next_task_id = max(task.id for task in self.tasks) + 1
        else:
            self.next_task_id = 1
    
    def save_tasks(self):
        """
        Save tasks to the file.
        """
        self.file_handler.save_tasks(self.tasks)
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks.
        
        Returns:
            A list of all Task objects
        """
        return self.tasks
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def add_task(
        self, 
        title: str, 
        description: Optional[str] = None, 
        priority: str = "medium", 
        category: Optional[str] = None, 
        due_date: Optional[str] = None,
        recurring: Optional[Dict[str, Any]] = None
    ) -> Task:
        """
        Add a new task.
        
        Args:
            title: Task title (required, non-empty)
            description: Optional task description (nullable)
            priority: Priority level - "high", "medium", or "low" (default: "medium")
            category: Category/Tag - "work", "home", "study" or custom (nullable)
            due_date: Optional due date (ISO format: YYYY-MM-DD, nullable)
            recurring: Recurrence pattern (nullable, structure: {"type": "daily|weekly|monthly", "interval": int})
            
        Returns:
            The newly created Task object
        """
        # Validate inputs
        if not validate_task_title(title):
            raise ValueError("Invalid task title")
        
        if not validate_task_priority(priority):
            raise ValueError("Invalid task priority")
        
        if not validate_task_category(category):
            raise ValueError("Invalid task category")
        
        if not validate_task_due_date(due_date):
            raise ValueError("Invalid task due date")
        
        if not validate_task_recurring(recurring):
            raise ValueError("Invalid task recurring pattern")
        
        # Create a new task with the next available ID
        task = Task(
            id=self.next_task_id,
            title=title,
            description=description,
            priority=priority,
            category=category,
            due_date=due_date,
            recurring=recurring
        )
        
        # Add the task to the list
        self.tasks.append(task)
        
        # Increment the next task ID
        self.next_task_id += 1
        
        # Save tasks to file
        self.save_tasks()
        
        return task
    
    def update_task(
        self, 
        task_id: int, 
        title: Optional[str] = None, 
        description: Optional[str] = None, 
        status: Optional[str] = None, 
        priority: Optional[str] = None, 
        category: Optional[str] = None, 
        due_date: Optional[str] = None,
        recurring: Optional[Dict[str, Any]] = None
    ) -> Optional[Task]:
        """
        Update an existing task.
        
        Args:
            task_id: The ID of the task to update
            title: New task title (optional)
            description: New task description (optional)
            status: New task status (optional)
            priority: New task priority (optional)
            category: New task category (optional)
            due_date: New task due date (optional)
            recurring: New task recurring pattern (optional)
            
        Returns:
            The updated Task object if successful, None if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        
        # Update fields if provided
        if title is not None:
            if not validate_task_title(title):
                raise ValueError("Invalid task title")
            task.title = title
        
        if description is not None:
            task.description = description
        
        if status is not None:
            if not validate_task_status(status):
                raise ValueError("Invalid task status")
            task.status = status
        
        if priority is not None:
            if not validate_task_priority(priority):
                raise ValueError("Invalid task priority")
            task.priority = priority
        
        if category is not None:
            if not validate_task_category(category):
                raise ValueError("Invalid task category")
            task.category = category
        
        if due_date is not None:
            if not validate_task_due_date(due_date):
                raise ValueError("Invalid task due date")
            task.due_date = due_date
        
        if recurring is not None:
            if not validate_task_recurring(recurring):
                raise ValueError("Invalid task recurring pattern")
            task.recurring = recurring
        
        # Validate the updated task
        task.validate()
        
        # Save tasks to file
        self.save_tasks()
        
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was deleted, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        
        self.tasks.remove(task)
        
        # Save tasks to file
        self.save_tasks()
        
        return True
    
    def mark_task_complete(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as complete.
        
        Args:
            task_id: The ID of the task to mark as complete
            
        Returns:
            The updated Task object if successful, None if task not found
        """
        return self.update_task(task_id, status="completed")
    
    def mark_task_pending(self, task_id: int) -> Optional[Task]:
        """
        Mark a task as pending.
        
        Args:
            task_id: The ID of the task to mark as pending
            
        Returns:
            The updated Task object if successful, None if task not found
        """
        return self.update_task(task_id, status="pending")
    
    def search_tasks(self, search_term: str) -> List[Task]:
        """
        Search tasks by title or description.
        
        Args:
            search_term: The term to search for in task titles and descriptions
            
        Returns:
            A list of Task objects that match the search term
        """
        search_term_lower = search_term.lower()
        matching_tasks = []
        
        for task in self.tasks:
            if (search_term_lower in task.title.lower() or 
                (task.description and search_term_lower in task.description.lower())):
                matching_tasks.append(task)
        
        return matching_tasks
    
    def filter_tasks(self, status: Optional[str] = None, priority: Optional[str] = None, category: Optional[str] = None) -> List[Task]:
        """
        Filter tasks by status, priority, or category.
        
        Args:
            status: Filter by task status (optional)
            priority: Filter by task priority (optional)
            category: Filter by task category (optional)
            
        Returns:
            A list of Task objects that match the filter criteria
        """
        filtered_tasks = []
        
        for task in self.tasks:
            match = True
            
            if status is not None and task.status != status:
                match = False
            
            if priority is not None and task.priority != priority:
                match = False
            
            if category is not None and task.category != category:
                match = False
            
            if match:
                filtered_tasks.append(task)
        
        return filtered_tasks
    
    def sort_tasks(self, sort_by: str = "created_date", reverse: bool = True) -> List[Task]:
        """
        Sort tasks by a specified attribute.
        
        Args:
            sort_by: The attribute to sort by (default: "created_date")
            reverse: Whether to sort in descending order (default: True)
            
        Returns:
            A list of Task objects sorted by the specified attribute
        """
        valid_sort_fields = ["title", "priority", "created_date", "due_date"]
        
        if sort_by not in valid_sort_fields:
            raise ValueError(f"Invalid sort field. Valid fields: {valid_sort_fields}")
        
        # Define a key function for sorting
        def sort_key(task):
            value = getattr(task, sort_by)
            # Handle None values by returning a default value
            if value is None:
                if sort_by == "priority":
                    # For priority, None would be treated as medium
                    return "medium"
                elif sort_by == "due_date" or sort_by == "created_date":
                    # For dates, None would be treated as a very early date
                    return "1970-01-01"
                else:
                    # For other fields, None would be treated as an empty string
                    return ""
            return value
        
        return sorted(self.tasks, key=sort_key, reverse=reverse)