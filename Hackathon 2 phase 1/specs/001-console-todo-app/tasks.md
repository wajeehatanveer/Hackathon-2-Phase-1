# Tasks: Console-Based Todo Application

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directory structure per implementation plan
- [X] T002 Create main.py file with basic application entry point
- [X] T003 [P] Create models directory and task.py file
- [X] T004 [P] Create persistence directory and file_handler.py file
- [X] T005 [P] Create ui directory and console_ui.py file
- [X] T006 [P] Create utils directory and validators.py file
- [X] T007 [P] Create tests directory for unit tests

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T008 Create Task class in todo_app/models/task.py with all required attributes
- [X] T009 [P] Create file handling functions in todo_app/persistence/file_handler.py
- [X] T010 [P] Create basic console UI functions in todo_app/ui/console_ui.py
- [X] T011 [P] Create input validation functions in todo_app/utils/validators.py
- [X] T012 Create TaskManager class in todo_app/task_manager.py with basic structure

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add tasks with title and description, and view all tasks in a numbered list

**Independent Test**: The application allows users to add a new task with a title and optional description, and then displays all tasks in a numbered list format. Users can verify that their tasks are saved and displayed correctly.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

- [ ] T013 [P] [US1] Create unit tests for Task model in tests/test_models.py
- [ ] T014 [P] [US1] Create tests for file persistence in tests/test_persistence.py

### Implementation for User Story 1

- [X] T015 [P] [US1] Implement Task class with all attributes and validation in todo_app/models/task.py
- [X] T016 [US1] Implement add_task method in TaskManager class in todo_app/task_manager.py
- [X] T017 [US1] Implement get_all_tasks method in TaskManager class in todo_app/task_manager.py
- [X] T018 [US1] Implement save_tasks_to_file function in todo_app/persistence/file_handler.py
- [X] T019 [US1] Implement load_tasks_from_file function in todo_app/persistence/file_handler.py
- [X] T020 [US1] Implement main menu display function in todo_app/ui/console_ui.py
- [X] T021 [US1] Implement add task UI flow in todo_app/ui/console_ui.py
- [X] T022 [US1] Implement view tasks UI flow in todo_app/ui/console_ui.py
- [X] T023 [US1] Integrate TaskManager with file persistence in todo_app/task_manager.py
- [X] T024 [US1] Connect main menu to task operations in todo_app/main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Update and Delete Tasks (Priority: P2)

**Goal**: Enable users to update or delete tasks by ID to keep their todo list current and accurate

**Independent Test**: The application allows users to select a task by ID and either update its details or delete it entirely. The changes are reflected in the task list.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T025 [P] [US2] Create tests for update and delete functionality in tests/test_task_manager.py

### Implementation for User Story 2

- [X] T026 [US2] Implement update_task method in TaskManager class in todo_app/task_manager.py
- [X] T027 [US2] Implement delete_task method in TaskManager class in todo_app/task_manager.py
- [X] T028 [US2] Implement update task UI flow in todo_app/ui/console_ui.py
- [X] T029 [US2] Implement delete task UI flow in todo_app/ui/console_ui.py
- [X] T030 [US2] Connect update/delete operations to main menu in todo_app/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks as Complete (Priority: P3)

**Goal**: Enable users to toggle task status between pending and completed to track progress

**Independent Test**: The application allows users to toggle the status of a task between pending and completed. The status change is reflected in the task list.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T031 [P] [US3] Create tests for status toggle functionality in tests/test_task_manager.py

### Implementation for User Story 3

- [X] T032 [US3] Implement mark_task_complete method in TaskManager class in todo_app/task_manager.py
- [X] T033 [US3] Implement mark_task_pending method in TaskManager class in todo_app/task_manager.py
- [X] T034 [US3] Implement status toggle UI flow in todo_app/ui/console_ui.py
- [X] T035 [US3] Connect status toggle operations to main menu in todo_app/main.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Prioritize and Categorize Tasks (Priority: P4)

**Goal**: Enable users to assign priority levels and categories to tasks for better organization

**Independent Test**: The application allows users to assign priority levels (High, Medium, Low) and categories (Work, Home, Study) to tasks. These attributes are displayed when viewing the task list.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T036 [P] [US4] Create tests for priority and category functionality in tests/test_task_manager.py

### Implementation for User Story 4

- [X] T037 [US4] Enhance Task class to support priority and category in todo_app/models/task.py
- [X] T038 [US4] Implement set_task_priority method in TaskManager class in todo_app/task_manager.py
- [X] T039 [US4] Implement set_task_category method in TaskManager class in todo_app/task_manager.py
- [X] T040 [US4] Update UI to allow priority and category assignment in todo_app/ui/console_ui.py
- [X] T041 [US4] Update task display to show priority and category in todo_app/ui/console_ui.py

**Checkpoint**: At this point, User Stories 1-4 should all work independently

---

## Phase 7: User Story 5 - Search, Filter, and Sort Tasks (Priority: P5)

**Goal**: Enable users to search, filter, and sort tasks for better organization and usability

**Independent Test**: The application allows users to search tasks by keyword, filter by status/priority/category, and sort by priority or title. The results are displayed according to the selected criteria.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T042 [P] [US5] Create tests for search, filter, and sort functionality in tests/test_task_manager.py

### Implementation for User Story 5

- [X] T043 [US5] Implement search_tasks method in TaskManager class in todo_app/task_manager.py
- [X] T044 [US5] Implement filter_tasks method in TaskManager class in todo_app/task_manager.py
- [X] T045 [US5] Implement sort_tasks method in TaskManager class in todo_app/task_manager.py
- [X] T046 [US5] Implement search UI flow in todo_app/ui/console_ui.py
- [X] T047 [US5] Implement filter UI flow in todo_app/ui/console_ui.py
- [X] T048 [US5] Implement sort UI flow in todo_app/ui/console_ui.py
- [X] T049 [US5] Connect search/filter/sort operations to main menu in todo_app/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Advanced Features - Due Dates and Recurring Tasks

**Goal**: Implement due dates and recurring tasks functionality

**Independent Test**: The application allows users to assign due dates to tasks and mark overdue tasks clearly in the list. It also supports recurring tasks that repeat daily or weekly.

### Tests for Advanced Features (OPTIONAL - only if tests requested) ⚠️

- [ ] T050 [P] Create tests for due date and recurring task functionality in tests/test_task_manager.py

### Implementation for Advanced Features

- [X] T051 Enhance Task class to support due_date and recurring attributes in todo_app/models/task.py
- [X] T052 Implement set_task_due_date method in TaskManager class in todo_app/task_manager.py
- [X] T053 Implement set_recurring_task method in TaskManager class in todo_app/task_manager.py
- [X] T054 Implement overdue task detection in TaskManager class in todo_app/task_manager.py
- [X] T055 Update UI to allow due date assignment in todo_app/ui/console_ui.py
- [X] T056 Update UI to show overdue tasks clearly in todo_app/ui/console_ui.py
- [X] T057 Update UI to allow recurring task setup in todo_app/ui/console_ui.py

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T058 [P] Update documentation in docs/
- [X] T059 Code cleanup and refactoring
- [X] T060 Performance optimization across all stories
- [X] T061 [P] Additional unit tests (if requested) in tests/unit/
- [X] T062 Security hardening
- [X] T063 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P5)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Create unit tests for Task model in tests/test_models.py"
Task: "Create tests for file persistence in tests/test_persistence.py"

# Launch all models for User Story 1 together:
Task: "Implement Task class with all attributes and validation in todo_app/models/task.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence