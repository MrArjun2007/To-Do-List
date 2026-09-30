"""Core task operations using a list of dictionaries."""
from validation import read_nonempty, read_task_id

def add_task(tasks, next_id):
    title = read_nonempty("Enter task name: ")
    task = {"id": next_id, "title": title, "completed": False}
    tasks.append(task)
    print("Task added successfully. Task ID:", next_id)
    return next_id + 1

def show_tasks(tasks, view):
    found = False
    print("\n---", view.title(), "Tasks ---")
    for task in tasks:
        if view == "all" or (view == "pending" and not task["completed"]) or (view == "completed" and task["completed"]):
            status = "Completed" if task["completed"] else "Pending"
            print("ID:", task["id"], "| Task:", task["title"], "| Status:", status)
            found = True
    if not found:
        print("No tasks to display.")

def complete_task(tasks):
    if len(tasks) == 0:
        print("There are no tasks.")
        return
    task_id = read_task_id("Enter task ID to complete: ")
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("This task is already completed.")
            else:
                task["completed"] = True
                print("Task marked as completed.")
            return
    print("Task ID not found.")

def delete_task(tasks):
    if len(tasks) == 0:
        print("There are no tasks.")
        return
    task_id = read_task_id("Enter task ID to delete: ")
    for index in range(len(tasks)):
        if tasks[index]["id"] == task_id:
            del tasks[index]
            print("Task deleted successfully.")
            return
    print("Task ID not found.")
