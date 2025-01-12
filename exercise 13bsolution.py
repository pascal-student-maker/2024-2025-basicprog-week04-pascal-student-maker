def count_elements_within_interval(collection:list,minimum,maximum)-> int:
    count = 0
    for element in collection:
        if minimum <= element <= maximum:
          count+= 1
    return count
List1 =  [10, 20, 30, 40, 40, 40, 70, 80, 99]     
List2 =  ['a', 'b', 'c', 'd', 'e', 'f']   
minimum = input("Enter a minimum:")
maximum = input("Enter a maximum:")

if minimum.isdigit() and maximum.isdigit():
    minimum = int(minimum)
    maximum = int(maximum)
    print(f"The number of elements between {minimum} and {maximum} is: {count_elements_within_interval(List1, minimum, maximum)}")
elif minimum.isalpha() and maximum.isalpha():
    minimum = str(minimum)
    maximum = str(maximum)
    print(f"The number of elements between {minimum} and {maximum} is: {count_elements_within_interval(List2, minimum, maximum)}")

