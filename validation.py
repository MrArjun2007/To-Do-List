"""Input validation using loops and conditionals."""

def read_nonempty(prompt):
    value = input(prompt).strip()
    while value == "":
        print("Input cannot be empty.")
        value = input(prompt).strip()
    return value

def read_choice(prompt, valid_choices):
    value = input(prompt).strip()
    while value not in valid_choices:
        print("Invalid choice. Please select a listed option.")
        value = input(prompt).strip()
    return value

def read_task_id(prompt):
    value = input(prompt).strip()
    while not value.isdigit() or int(value) <= 0:
        print("Enter a positive whole-number task ID.")
        value = input(prompt).strip()
    return int(value)
