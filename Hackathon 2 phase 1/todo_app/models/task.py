"""
Task model for the Console-Based Todo Application.

This module defines the Task class with all required attributes and validation.
"""
from datetime import datetime
from typing import Optional, Dict, Any


class Task:
    """
    Represents a task in the todo application.
    """
    
    def __init__(self, 
                 id: int, 
                 title: str, 
                 description: Optional[str] = None, 
                 status: str = "pending", 
                 priority: str = "medium", 
                 category: Optional[str] = None, 
                 created_date: Optional[str] = None, 
                 due_date: Optional[str] = None, 
                 recurring: Optional[Dict[str, Any]] = None):
        """
        Initialize a Task instance.
        
        Args:
            id: Unique identifier for the task (auto-generated)
            title: Task title (required, non-empty)
            description: Optional task description (nullable)
            status: Task status - "pending" or "completed" (default: "pending")
            priority: Priority level - "high", "medium", or "low" (default: "medium")
            category: Category/Tag - "work", "home", "study" or custom (nullable)
            created_date: Date when task was created (ISO format: YYYY-MM-DD)
            due_date: Optional due date (ISO format: YYYY-MM-DD, nullable)
            recurring: Recurrence pattern (nullable, structure: {"type": "daily|weekly|monthly", "interval": int})
        """
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.category = category
        self.created_date = created_date or datetime.now().strftime("%Y-%m-%d")
        self.due_date = due_date
        self.recurring = recurring
        
        # Validate the task attributes
        self.validate()
    
    def validate(self):
        """
        Validate the task attributes according to the defined rules.
        """
        # Validate title
        if not self.title or not isinstance(self.title, str) or len(self.title) < 1 or len(self.title) > 200:
            raise ValueError("Title must be a string between 1 and 200 characters")
        
        # Validate status
        if self.status not in ["pending", "completed"]:
            raise ValueError("Status must be either 'pending' or 'completed'")
        
        # Validate priority
        if self.priority not in ["high", "medium", "low"]:
            raise ValueError("Priority must be 'high', 'medium', or 'low'")
        
        # Validate category if provided
        if self.category and (not isinstance(self.category, str) or len(self.category) < 1 or len(self.category) > 50):
            raise ValueError("Category must be a string between 1 and 50 characters if provided")
        
        # Validate due date if provided
        if self.due_date:
            try:
                due_date_obj = datetime.strptime(self.due_date, "%Y-%m-%d")
                created_date_obj = datetime.strptime(self.created_date, "%Y-%m-%d")
                if due_date_obj < created_date_obj:
                    raise ValueError("Due date must be in the future if provided")
            except ValueError:
                raise ValueError("Due date must be in ISO format (YYYY-MM-DD)")
        
        # Validate recurring pattern if provided
        if self.recurring:
            if not isinstance(self.recurring, dict):
                raise ValueError("Recurring pattern must be a dictionary")
            
            if "type" not in self.recurring or "interval" not in self.recurring:
                raise ValueError("Recurring pattern must have 'type' and 'interval' keys")
            
            if self.recurring["type"] not in ["daily", "weekly", "monthly"]:
                raise ValueError("Recurring type must be 'daily', 'weekly', or 'monthly'")
            
            if not isinstance(self.recurring["interval"], int) or self.recurring["interval"] <= 0:
                raise ValueError("Recurring interval must be a positive integer")
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the task to a dictionary representation.
        
        Returns:
            A dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "category": self.category,
            "created_date": self.created_date,
            "due_date": self.due_date,
            "recurring": self.recurring
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """
        Create a Task instance from a dictionary representation.
        
        Args:
            data: Dictionary representation of a task
            
        Returns:
            A Task instance
        """
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description"),
            status=data.get("status", "pending"),
            priority=data.get("priority", "medium"),
            category=data.get("category"),
            created_date=data.get("created_date"),
            due_date=data.get("due_date"),
            recurring=data.get("recurring")
        )
    
    def __str__(self) -> str:
        """
        String representation of the task.

        Returns:
            A formatted string representation of the task
        """
        status_icon = "X" if self.status == "completed" else "O"
        return f"[{status_icon}] [{self.id}] {self.title} ({self.priority}) - {self.status}"
    
    def __repr__(self) -> str:
        """
        Detailed string representation of the task.
        
        Returns:
            A detailed string representation of the task
        """
        return f"Task(id={self.id}, title='{self.title}', status='{self.status}', priority='{self.priority}')"