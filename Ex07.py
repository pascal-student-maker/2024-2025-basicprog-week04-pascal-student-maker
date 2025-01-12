def get_info_list(name:str,collection:list) -> str:
    result = f" {name}\n"
    for i  in range(len(collection)):
        result += f" {collection[i]} is  on position {i}\n"
        return result
    
        
        
        
collection1 = [12, 45, -9, -15]
collection2 = [12.23, 45.1, 9.478, 15.125, -3.14]
collection3 = ["Joerie", "Marie", "Henk", "Stijn"]

# Call the function for multiple lists
print(get_info_list("Collection Non-decimal numbers", collection1))
print(get_info_list("Collection Decimal numbers", collection2))
print(get_info_list("Collection Strings", collection3))
        
        