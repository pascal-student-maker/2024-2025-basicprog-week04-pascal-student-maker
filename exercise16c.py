def give_even_positions(list1:list) -> list:
    new_list = []
    for element in list1[::2]:
        print(element)
        new_list.append(element)
        
    return new_list 

original_list = [ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90] 
print(f" Original list: {original_list}")
print(f" The elements in the even positions are: {give_even_positions(original_list)}")  