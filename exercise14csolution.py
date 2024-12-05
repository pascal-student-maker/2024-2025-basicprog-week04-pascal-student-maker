#exercise14csolution.py

def give_common_elements(list1, list2):
    common_elements = []
    for x in list1:
        if x in list2 and x not in common_elements:
            common_elements.append(x)
    common_elements.sort()
    return common_elements

# Test cases
list1 = [78, 4, 5, 6, 4]
list2 = [89, 78, 4]
print(f"Common elements: {give_common_elements(list1, list2)}")

list3 = ['Tamara', 'Delfien', 'Elke', 'Marijn']
list4 = ['Natasja', 'Mieke', 'Tamara', 'Elke', 'Carine']
print(f"Common elements: {give_common_elements(list3, list4)}")