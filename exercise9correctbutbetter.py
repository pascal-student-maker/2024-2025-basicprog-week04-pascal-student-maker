def max_and_min_from_list(numbers: list) -> tuple:
    """Return the max and min values from a list."""
    return max(numbers), min(numbers)

# Example 1: Numbers
print("\nA list can also be used as a parameter.")  
list_numbers = [100, 200, 300, 400, 500, 600, 700, 800] 
print(f"Original list: {list_numbers}")

# Get max and min
max_value, min_value = max_and_min_from_list(list_numbers)
print(f"From {list_numbers}, the max is {max_value} and the min is {min_value}.")

# Example 2: Months
print("\nA list can also be used as a parameter.")  
list_month = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
print(f"Original list: {list_month}")

# Get max and min
max_value, min_value = max_and_min_from_list(list_month)
print(f"From {list_month}, the max is {max_value} and the min is {min_value}.")
