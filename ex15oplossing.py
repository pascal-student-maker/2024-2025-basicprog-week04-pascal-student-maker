#ex.15 oplossing

def remove_duplicates(input_list):
    return list(set(input_list))

# Input list
test = ["A", 89, 78, 4, "A", "test", 4]

# Call the function and print the results
print(f"Original list: {test}")
print(f"Without duplicates: {remove_duplicates(test)}")
