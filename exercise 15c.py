#exercise 15c
def remove_duplicates(list1):
    remove_duplicates = []
    for x in list1:
        if x not in remove_duplicates:
            remove_duplicates.append(x)
    return remove_duplicates

list1 =  ['A', 89, 78, 4, 'A', 'test', 4]
print(f"Without duplicates {remove_duplicates(list1)}")
