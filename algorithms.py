"""Small fundamental algorithms used by the project."""

def count_items(items):
    """Count values by traversing a sequence."""
    count = 0
    for item in items:
        count = count + 1
    return count

def sum_values(values):
    """Calculate a total using a running summation."""
    total = 0
    for value in values:
        total = total + value
    return total
