# Data Model: Console-Based Todo Application

## Task Entity

### Attributes
- **id**: (int) Unique identifier for the task (auto-generated)
- **title**: (str) Task title (required, non-empty)
- **description**: (str) Optional task description (nullable)
- **status**: (str) Task status - "pending" or "completed" (default: "pending")
- **priority**: (str) Priority level - "high", "medium", or "low" (default: "medium")
- **category**: (str) Category/Tag - "work", "home", "study" or custom (nullable)
- **created_date**: (str) Date when task was created (ISO format: YYYY-MM-DD)
- **due_date**: (str) Optional due date (ISO format: YYYY-MM-DD, nullable)
- **recurring**: (dict) Recurrence pattern (nullable, structure: {"type": "daily|weekly|monthly", "interval": int})

### Validation Rules
- Title must be between 1-200 characters
- Status must be one of: "pending", "completed"
- Priority must be one of: "high", "medium", "low"
- Category must be 1-50 characters if provided
- Due date must be in the future if provided
- Recurring pattern must have valid type and positive interval if provided

### State Transitions
- A task can transition from "pending" to "completed"
- A task can transition from "completed" to "pending"
- No other state transitions are allowed

## Task List Structure

### In-Memory Representation
- A Python list containing Task entities
- Tasks are ordered by creation date (newest first) by default
- Each task ID is unique within the list

### JSON File Structure
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Sample task",
      "description": "Sample description",
      "status": "pending",
      "priority": "medium",
      "category": "work",
      "created_date": "2025-01-01",
      "due_date": "2025-01-10",
      "recurring": {
        "type": "daily",
        "interval": 1
      }
    }
  ],
  "next_id": 2
}
```

### File Location
- Default file: `tasks.json` in the application directory
- File is created if it doesn't exist
- File is updated after every add, update, or delete operation