#exercise 14
def give_common_elements(list1:list,list2:list) -> list:
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
            common_elements.sort()
            common_elements = list(set(common_elements))
            
    return common_elements

list1 = [78, 4, 5, 6, 4]
list2 = [89, 78, 4]  
List3 =  ['Tamara', 'Delfien', 'Elke', 'Marijn']
List4 = ['Natasja', 'Mieke', 'Tamara', 'Elke', 'Carine']

print(f" the common elements are {give_common_elements(list1,list2)}") 
print(f" the common elements are {give_common_elements(List3,List4)}")   
  
   
           