"""Summary calculations for the task list."""
from algorithms import count_items, sum_values

def show_summary(tasks):
    completed_flags = []
    pending_flags = []
    for task in tasks:
        if task["completed"]:
            completed_flags.append(1)
        else:
            pending_flags.append(1)

    total = count_items(tasks)
    completed = sum_values(completed_flags)
    pending = sum_values(pending_flags)

    print("\n--- Task Summary ---")
    print("Total tasks:", total)
    print("Completed tasks:", completed)
    print("Pending tasks:", pending)
