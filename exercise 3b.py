def create_new_friends() -> list[str]:
    friends = []
    
    while True:
        name = str(input(" Enter a friend's name, or exit with an empty field:>")).strip()
        if name == "":
            break
        
        friends.append(name)
        
    return friends 



friends = create_new_friends() 
print(f" Your friends are {friends}")  


        
            
            
      