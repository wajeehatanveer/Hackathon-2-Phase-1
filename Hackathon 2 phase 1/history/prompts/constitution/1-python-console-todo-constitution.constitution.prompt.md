---
id: 1
title: Python Console Todo Constitution
stage: constitution
date: 2025-01-01
surface: agent
model: gpt-4
feature: python-console-todo
branch: main
user: user
command: /sp.constitution
labels: ["constitution", "todo-app", "python"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:

---

## Prompt

```
/sp.constitution You are building a Python console-based Todo application.

Rules & Constraints:
- The application MUST be console-based (no GUI, no web, no mobile).
- Language: Python only.
- Code must be clean, readable, and beginner-friendly.
- Use functions and basic object-oriented concepts where helpful.
- No external frameworks (only Python standard library).
- Data persistence should be simple (text file or JSON file).
- The app must run fully from the terminal.
- User interaction must be menu-driven.
- Error handling must be included for invalid inputs.
- Follow a clear feature progression: Basic → Intermediate → Advanced.
- No unnecessary features beyond the defined scope.
- Focus on correctness, clarity, and stability over complexity.
```

## Response snapshot

The Python Console Todo Application Constitution has been successfully created with the following details:

**New Version**: 1.0.0 (initial version)
**Bump Rationale**: This is the initial constitution for the Python Console Todo Application project, establishing the foundational principles and constraints.

**Summary of Changes**:
- Created a comprehensive constitution with 6 core principles:
  1. Console-First Interface
  2. Python Standard Library Only
  3. Clean, Beginner-Friendly Code
  4. Simple Data Persistence
  5. Error Handling
  6. Feature Progression
- Added two additional sections: Development Constraints and Quality Standards
- Established governance rules for the project
- Set version to 1.0.0 with ratification date of 2025-01-01

**Files Updated**:
- .specify/memory/constitution.md - The main constitution file

**Follow-up Items**: None required

**Suggested Commit Message**: `docs: add constitution for Python Console Todo Application v1.0.0`

The constitution aligns with your requirements for a Python console-based Todo application that uses only the standard library, is beginner-friendly, and follows a clear feature progression from basic to advanced functionality.

## Outcome

- ✅ Impact: Created initial constitution for Python console todo app
- 🧪 Tests: No tests run
- 📁 Files: Updated constitution.md file
- 🔁 Next prompts: Build specification based on constitution
- 🧠 Reflection: Successfully created constitution following template requirements

## Evaluation notes (flywheel)

- Failure modes observed: None observed
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment: Begin spec creation