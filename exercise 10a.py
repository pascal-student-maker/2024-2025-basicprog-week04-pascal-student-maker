#exercise 10a

def sum_of_list(numbers: list[int]) -> int:
    total = 0
    for number in numbers:
        total = total + number
    return total    

my_favorite_numbers = [10,14,18,22,26,30]
print(
    f"Check after the function sum_of_list: the sum of is {sum_of_list(my_favorite_numbers)}"
)
