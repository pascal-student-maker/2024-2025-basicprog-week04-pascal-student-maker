list1 = [78, 4, 5, 6, 4]
list2 = [89, 78, 4]

common_elements = []
for element in list1:
    if element in list2:
        common_elements.append(element)

print(common_elements)  # Output: [78, 4] #chatgpt solution