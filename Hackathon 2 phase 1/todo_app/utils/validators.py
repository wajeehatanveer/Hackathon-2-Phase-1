"""
Input validators for the Console-Based Todo Application.

This module provides input validation utilities for the application.
"""
from typing import Optional
import re
from datetime import datetime


def validate_task_title(title: str) -> bool:
    """
    Validate the task title according to the defined rules.
    
    Args:
        title: The task title to validate
        
    Returns:
        True if the title is valid, False otherwise
    """
    if not title or not isinstance(title, str):
        return False
    
    if len(title) < 1 or len(title) > 200:
        return False
    
    return True


def validate_task_status(status: str) -> bool:
    """
    Validate the task status according to the defined rules.
    
    Args:
        status: The task status to validate
        
    Returns:
        True if the status is valid, False otherwise
    """
    return status in ["pending", "completed"]


def validate_task_priority(priority: str) -> bool:
    """
    Validate the task priority according to the defined rules.
    
    Args:
        priority: The task priority to validate
        
    Returns:
        True if the priority is valid, False otherwise
    """
    return priority in ["high", "medium", "low"]


def validate_task_category(category: Optional[str]) -> bool:
    """
    Validate the task category according to the defined rules.
    
    Args:
        category: The task category to validate (can be None)
        
    Returns:
        True if the category is valid, False otherwise
    """
    if category is None:
        return True
    
    if not isinstance(category, str):
        return False
    
    if len(category) < 1 or len(category) > 50:
        return False
    
    return True


def validate_task_due_date(due_date: Optional[str]) -> bool:
    """
    Validate the task due date according to the defined rules.
    
    Args:
        due_date: The task due date to validate (can be None)
        
    Returns:
        True if the due date is valid, False otherwise
    """
    if due_date is None:
        return True
    
    if not isinstance(due_date, str):
        return False
    
    try:
        # Check if the date is in the correct format (YYYY-MM-DD)
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_task_recurring(recurring: Optional[dict]) -> bool:
    """
    Validate the task recurring pattern according to the defined rules.
    
    Args:
        recurring: The task recurring pattern to validate (can be None)
        
    Returns:
        True if the recurring pattern is valid, False otherwise
    """
    if recurring is None:
        return True
    
    if not isinstance(recurring, dict):
        return False
    
    if "type" not in recurring or "interval" not in recurring:
        return False
    
    if recurring["type"] not in ["daily", "weekly", "monthly"]:
        return False
    
    if not isinstance(recurring["interval"], int) or recurring["interval"] <= 0:
        return False
    
    return True


def validate_date_format(date_string: str) -> bool:
    """
    Validate if a string is in the correct date format (YYYY-MM-DD).
    
    Args:
        date_string: The date string to validate
        
    Returns:
        True if the date format is valid, False otherwise
    """
    if not isinstance(date_string, str):
        return False
    
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_positive_integer(value: str) -> bool:
    """
    Validate if a string represents a positive integer.
    
    Args:
        value: The string to validate
        
    Returns:
        True if the value is a positive integer, False otherwise
    """
    if not isinstance(value, str):
        return False
    
    try:
        num = int(value)
        return num > 0
    except ValueError:
        return False


def sanitize_input(input_str: str) -> str:
    """
    Sanitize user input by removing potentially harmful characters.
    
    Args:
        input_str: The input string to sanitize
        
    Returns:
        The sanitized string
    """
    if not isinstance(input_str, str):
        return ""
    
    # Remove any potentially harmful characters
    # For now, just strip leading/trailing whitespace
    return input_str.strip()


def is_valid_email(email: str) -> bool:
    """
    Validate if a string is a valid email address format.
    This is a simple validation and not comprehensive.
    
    Args:
        email: The email string to validate
        
    Returns:
        True if the email format is valid, False otherwise
    """
    if not isinstance(email, str):
        return False
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None