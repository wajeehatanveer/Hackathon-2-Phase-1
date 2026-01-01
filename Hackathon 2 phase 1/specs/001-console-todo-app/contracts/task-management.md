# Task Management Contract

## Overview
This document defines the contract for task management operations in the Console-Based Todo Application. It specifies the expected behavior, inputs, and outputs for each operation.

## Task Structure
```
{
  "id": integer,
  "title": string,
  "description": string (optional),
  "status": "pending" | "completed",
  "priority": "high" | "medium" | "low",
  "category": string (optional),
  "created_date": string (YYYY-MM-DD),
  "due_date": string (YYYY-MM-DD, optional),
  "recurring": {
    "type": "daily" | "weekly" | "monthly",
    "interval": integer
  } (optional)
}
```

## Operations

### Add Task
- **Input**: Task title (required), description (optional), priority (optional, default: "medium"), category (optional), due_date (optional), recurring (optional)
- **Output**: New task with assigned ID and created_date
- **Validation**: Title must be 1-200 characters
- **Error cases**: Invalid input parameters

### View Tasks
- **Input**: Filter parameters (optional: status, priority, category, search term)
- **Output**: List of tasks matching criteria
- **Default**: All tasks sorted by creation date (newest first)
- **Error cases**: None

### Update Task
- **Input**: Task ID, fields to update
- **Output**: Updated task
- **Validation**: ID must exist, field values must be valid
- **Error cases**: Task ID not found, invalid field values

### Delete Task
- **Input**: Task ID
- **Output**: Confirmation of deletion
- **Validation**: ID must exist
- **Error cases**: Task ID not found

### Mark Task Complete
- **Input**: Task ID
- **Output**: Updated task with status "completed"
- **Validation**: ID must exist
- **Error cases**: Task ID not found

### Mark Task Pending
- **Input**: Task ID
- **Output**: Updated task with status "pending"
- **Validation**: ID must exist
- **Error cases**: Task ID not found

### Search Tasks
- **Input**: Search term
- **Output**: List of tasks containing the search term in title or description
- **Error cases**: None

### Filter Tasks
- **Input**: Filter criteria (status, priority, category)
- **Output**: List of tasks matching all criteria
- **Error cases**: Invalid filter values

### Sort Tasks
- **Input**: Sort criteria (by priority, by due date, by title, by creation date)
- **Output**: List of tasks sorted according to criteria
- **Error cases**: Invalid sort criteria