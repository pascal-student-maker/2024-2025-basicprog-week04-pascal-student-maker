def choose_random_list(list_month: list[str]) -> str:
    import random
    random.choice(list_month)
    return random.choice(list_month)

    
    
print("\nA list can also be used as an parameter.")  
list_month = ["January","February","March","April","May","June","July","August","September","October","November","December"] 
print(f"Orginal list: {list_month}")
random_month = choose_random_list(list_month)
print(f"check after function change list: {random_month}")


 



    
