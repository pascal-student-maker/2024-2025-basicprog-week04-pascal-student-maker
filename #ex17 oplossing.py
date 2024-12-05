#ex17 oplossing

import random

def choose_5_numbers(min_value, max_value):
  """Chooses 5 unique random numbers within a specified range.

  Args:
    min_value: The minimum value of the range.
    max_value: The maximum value of the range.

  Returns:
    A list of 5 unique random numbers.
  """

  numbers = set()
  while len(numbers) < 5:
    number = random.randint(min_value, max_value)
    numbers.add(number)
  return list(numbers)

min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

result = choose_5_numbers(min_value, max_value)
print(f"The five selected numbers in between are: {result}")