def give_even_positions(list1):
    even_positions = []
    odd_positions = []
    for i in range(len(list1)):
        if i % 2 == 0:
            even_positions.append(list1[i])
        else:
            odd_positions.append(list1[i])
    return even_positions

list1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
even_elements = give_even_positions(list1)

print(f"Original list: {list1}")
print(f"The elements in the even positions are: {even_elements}")        
        