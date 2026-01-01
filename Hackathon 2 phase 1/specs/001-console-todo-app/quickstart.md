# Quickstart Guide: Console-Based Todo Application

## Prerequisites
- Python 3.8 or higher
- No additional libraries required (using only Python standard library)

## Setup
1. Clone or download the application files
2. Navigate to the application directory
3. Ensure you have Python 3.8+ installed (`python --version`)

## Running the Application
```bash
python main.py
```

## Basic Usage
1. The application starts with a menu showing available options
2. Enter the number corresponding to your desired action
3. Follow the prompts to complete your task
4. Use option 0 to exit the application

## Available Features
- Add new tasks with title and optional description
- View all tasks in a numbered list
- Update existing tasks
- Delete tasks by ID
- Mark tasks as complete/incomplete
- Assign priorities and categories to tasks
- Search, filter, and sort tasks

## File Structure
- `main.py`: Entry point and main application loop
- `task_manager.py`: Core task management functionality
- `models/task.py`: Task data model
- `persistence/file_handler.py`: JSON file handling
- `ui/console_ui.py`: Console user interface
- `utils/validators.py`: Input validation utilities

## Data Storage
- Tasks are stored in `tasks.json` in the application directory
- The file is automatically created if it doesn't exist
- All changes are saved immediately to the file