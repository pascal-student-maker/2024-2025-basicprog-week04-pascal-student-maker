amount_workers = []
amount_clerks = []
amount_managers = []
total_salary = amount_salary = []
def create_program_salary(type_of_employee:str,salary:int):
    if type_of_employee == "W":
        amount_workers.append(type_of_employee)
        amount_salary.append(salary)
    elif type_of_employee == "C": 
        amount_clerks.append(type_of_employee) 
        amount_salary.append(salary)
    elif type_of_employee == "M":
        amount_managers.append(type_of_employee) 
        amount_salary.append(salary)
    else:
        print("Invalid category. Please Enter W,M,C")  
        
number_of_employees = int(input("Enter the amount of employees:"))

for _ in range(number_of_employees):
    type_of_employee = input("Specify the type of employee:> ")  
    salary = int(input("Enter the salary:>")) 
    create_program_salary(type_of_employee,salary)  

total_amount_employees = len(amount_clerks)  + len(amount_managers)  + len(amount_workers)  
print(f" Amount of the workers {len(amount_workers)}")
print(f" Amount of the clerks {len(amount_clerks)}")
print(f" Amount of the managers{len(amount_managers)}")
print(f" Total amount of employees: {total_amount_employees}")
print(f" Total amount of salary: {sum(amount_salary)}")




      
        
    
        
        
    


