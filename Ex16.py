# list1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(f"De elementen uit {list1} op de even posities zijn: {geef_even_posities(list1)}")

def give_even_positions(input_list):
       return list(input_list[0:9:2])
   
list1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"The elements  in the even positions are: {give_even_positions(list1)}")