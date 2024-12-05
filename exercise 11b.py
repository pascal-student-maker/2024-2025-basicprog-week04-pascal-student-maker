#exercise 11b

def average_of_list(numbers: list[int]) -> float:
    if numbers:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    else:
        return float('nan')

my_favorite_numbers = [10,14,18,22,26,30]
my_average_numbers = []
print(
    f"Check after the function averageof_list: the average of is {average_of_list(my_favorite_numbers)}"
)
print(
    f"Check after the function average_of_list: the average of is {average_of_list(my_average_numbers)}"  
)
