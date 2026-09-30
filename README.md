# Task List Management System

## Overview
Beginner level menu based task list management system for students written in Python programming language. It allows to add tasks, display all / pending / completed tasks, complete tasks, delete tasks and display statistics.

**Note:** Tasks are stored in memory while the application is running. They are destroyed upon application termination. The persistent storage is left out on purpose in order to keep implementation within the limits of the course syllabus.

## Functionalities
- Create task with auto generated ID
- View all tasks, pending tasks and completed tasks
- Mark task as completed
- Delete task
- Show statistics about task total count, completed and pending
- Validate user input and task names / IDs

## Syllabus topics involved
- Problem solving and top down design: separation of interface, operations, validation and reporting
- Algorithms: traversing, counting and summation
- Python fundamentals: values, data types, variables, expressions, statements, comments, modules and functions
- Flow control: if, elif, else, while, for
- Data structures: lists and dictionaries
- Input validation and simple error handling

Only necessary topics have been implemented in the application, other syllabus concepts haven't been forced into implementation.

## Technologies
- Python 3
- Python interpreter / terminal
- Git and GitHub
There is no need to install third-party packages.

## Structure of the project
```text
todo_list_github_project/
├── main.py
├── task_manager.py
├── reports.py
├── algorithms.py
├── validation.py
├── statement.md
├── design.md
└── tests/
    └── test_project.py
```

## Installation and execution of the code
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the folder with the project.
4. Type:
   ```bash
   python main.py
   ```
   On some systems, `python3 main.py` should be used instead.

## Tests
Run the provided basic tests:
```bash
python tests/test_project.py
```
Output:
```text
All basic tests passed.
```

## Sample workflow
1. Choose `1` to add a new task.
2. Input the task name, for example `Complete Python assignment`.
3. Choose `2` to see all tasks.
4. Choose `5` and input the task id to mark it as done.
5. Choose `7` to see the summary report.
6. Exit by choosing `0`.

## GitHub
Create a new GitHub repository, place these files in there, commit them and push the repository. Keep `README.md`, `statement.md` and `design.md` in the root of the repository.