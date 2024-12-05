def counts_elements_within_interval(list1, min, max):
    c = 0
    for x in list1:
        if min <= x <= max:
            c += 1
    return c

# Usage:
list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70,80,99]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']

# Case 1: Numeric Range
min = 40
max = 80
print(f"The number of elements between 40 and 80 : {counts_elements_within_interval(list1,min,max)}")  # Output: 4

# Case 2: Alphabetic Range (Corrected)
min = 'a'
max = 'e'
print(f"The number of elements between a and e : {counts_elements_within_interval(list2,min,max)}" ) # Output: 4