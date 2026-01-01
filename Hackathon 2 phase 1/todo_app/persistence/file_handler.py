"""
File handler for the Console-Based Todo Application.

This module handles JSON file operations for task persistence.
"""
import json
import os
from typing import List

from models.task import Task


class FileHandler:
    """
    Handles file operations for task persistence using JSON format.
    """

    def __init__(self, file_path: str = "tasks.json"):
        """
        Initialize the file handler with a specific file path.

        Args:
            file_path: Path to the JSON file for task storage (default: "tasks.json")
        """
        self.file_path = file_path
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """
        Ensure the tasks file exists, create it with empty structure if it doesn't.
        """
        if not os.path.exists(self.file_path):
            self.save_tasks([])

    def load_tasks(self) -> List[Task]:
        """
        Load tasks from the JSON file.

        Returns:
            A list of Task objects
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            tasks_data = data.get("tasks", [])
            next_id = data.get("next_id", 1)

            tasks = []
            for task_data in tasks_data:
                task = Task.from_dict(task_data)
                tasks.append(task)

            return tasks
        except FileNotFoundError:
            # If file doesn't exist, return empty list
            return []
        except json.JSONDecodeError:
            # If file is corrupted, return empty list
            print(f"Warning: {self.file_path} is corrupted. Starting with empty task list.")
            return []
        except Exception as e:
            print(f"Error loading tasks from {self.file_path}: {e}")
            return []

    def save_tasks(self, tasks: List[Task]):
        """
        Save tasks to the JSON file.

        Args:
            tasks: A list of Task objects to save
        """
        try:
            # Prepare data for JSON serialization
            tasks_data = [task.to_dict() for task in tasks]

            # Determine the next ID based on the highest ID in the current tasks
            next_id = 1
            if tasks:
                next_id = max(task.id for task in tasks) + 1

            data = {
                "tasks": tasks_data,
                "next_id": next_id
            }

            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving tasks to {self.file_path}: {e}")

    def get_next_task_id(self) -> int:
        """
        Get the next available task ID.

        Returns:
            The next available task ID
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data.get("next_id", 1)
        except (FileNotFoundError, json.JSONDecodeError):
            return 1