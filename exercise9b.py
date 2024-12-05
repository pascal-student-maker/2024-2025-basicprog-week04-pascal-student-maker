def choose_random_list(list_month: list[str]) -> str:
    list_month.random()
    
print("\nA list can also be used as an parameter.")  
month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"] 
print(f"Orginallist: {month_list}")
choose_random_list(month_list)
print(f"check after function change list: {choose_random_list}")


 



    
