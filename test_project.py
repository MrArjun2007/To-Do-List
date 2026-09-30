"""Simple validation tests for the project's core functions."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from algorithms import count_items, sum_values
from task_manager import add_task, complete_task, delete_task

def run_tests():
    assert count_items([]) == 0
    assert count_items([1, 2, 3]) == 3
    assert sum_values([]) == 0
    assert sum_values([1, 1, 1]) == 3

    tasks = []
    next_id = add_task_test(tasks, 1, "Read chapter")
    assert next_id == 2
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Read chapter"
    assert tasks[0]["completed"] is False

    tasks[0]["completed"] = True
    assert tasks[0]["completed"] is True
    del tasks[0]
    assert tasks == []
    print("All basic tests passed.")

def add_task_test(tasks, next_id, title):
    tasks.append({"id": next_id, "title": title, "completed": False})
    return next_id + 1

if __name__ == "__main__":
    run_tests()
