#exercise 14
def give_common_elements(list1,list2):
    for x in list1:
        for y in list2:
            if x ==y:
                result = "at least list1 and list2 element in common"
                return result
            print(result)
print(f" common elements: {give_common_elements([78,4,5,6,4],[89,78,4])}")
print(f" common elements: {give_common_elements(['Tamara', 'Delfien', 'Elke', 'Marijn'],['Natasja', 'Mieke', 'Tamara', 'Elke', 'Carine'])}")         