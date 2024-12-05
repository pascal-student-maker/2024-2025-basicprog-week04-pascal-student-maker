#homework 1 solution

# Improved homework1.py

def its_equal(list1, list2):
    """Checks if two lists contain the same elements, regardless of order.

    Args:
        list1 (list): The first list to compare.
        list2 (list): The second list to compare.

    Returns:
        bool: True if the lists contain the same elements, False otherwise.
    """

    # Check if lists have the same length (faster for unequal lengths)
    if len(list1) != len(list2):
        return False

    # Convert lists to sets for efficient element membership checks
    set1 = set(list1)
    set2 = set(list2)

    # Check if all elements in set1 are also in set2 (and vice versa)
    return set1 <= set2 and set2 <= set1

# Example usage
list1 = [10, 14, 2, 3, -10]
list2 = [-10, 3, 2, 10, 14]

if its_equal(list1, list2):
    print("Equal?: True")
else:
    print("Equal?: False")