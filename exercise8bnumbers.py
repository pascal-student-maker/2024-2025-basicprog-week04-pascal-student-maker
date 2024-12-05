def choose_random_list(list_numbers: list[int]) -> int:
    import random
    random.choice(list_numbers)
    return random.choice(list_numbers)

    
    
print("\nA list can also be used as an parameter.")  
list_numbers = [100,200,300,400,500,600.700,800] 
print(f"Orginal list: {list_numbers}")
random_number = choose_random_list(list_numbers)
print(f"check after function change list: {random_number}")


 



    
