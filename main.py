# main.py
# to-do list app, menu based
# (made this the main file, the rest is split into other files)

from task_manager import add_task, show_tasks, complete_task, delete_task
from reports import show_summary
from validation import read_choice

def print_menu():
    # prints the menu, called every loop
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add a task")
    print("2. Show all tasks")
    print("3. Show pending tasks")
    print("4. Show completed tasks")
    print("5. Mark a task as done")
    print("6. Delete a task")
    print("7. Summary")
    print("0. Exit")


def main():
    tasks = []   # everything is stored here, nothing saved to a file yet
    next_id = 1  # id for the next task, only goes up

    # TODO: maybe save tasks to a file later so they don't disappear

    while True:
        print_menu()

        # keeps asking until the input is valid
        choice = read_choice("Enter your choice: ", list("01234567"))

        if choice == "0":
            print("Thanks for using the To-Do List Manager. Bye!")
            break  # ends the program
        elif choice == "1":
            next_id = add_task(tasks, next_id)  # gives back the new id
        elif choice == "2":
            show_tasks(tasks, "all")
        elif choice == "3":
            show_tasks(tasks, "pending")   # not done yet
        elif choice == "4":
            show_tasks(tasks, "completed") # already done
        elif choice == "5":
            complete_task(tasks)   # asks for the id inside the function
        elif choice == "6":
            delete_task(tasks)
        elif choice == "7":
            show_summary(tasks)


# only run main when this file is run directly
if __name__ == "__main__":
    main()