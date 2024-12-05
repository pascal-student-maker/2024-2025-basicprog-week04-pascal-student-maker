#ex 18 solutin 

workers_salary = []
clerks_salary = []
managers_salary = []

while True:
    employee_type = input("Specify the type of employee (W: Worker, C: Clerk, M: Manager): ")
    if employee_type.upper() not in ['W', 'C', 'M']:
        print("Invalid employee type. Please enter W, C, or M.")
        continue

    salary = float(input("Enter the salary: "))

    if employee_type.upper() == 'W':
        workers_salary.append(salary)
    elif employee_type.upper() == 'C':
        clerks_salary.append(salary)
    else:
        managers_salary.append(salary)

    more_employees = input("Do you want to enter another employee? (yes/no): ")
    if more_employees.lower() != 'yes':
        break

# Calculate totals and print results
total_workers = len(workers_salary)
total_clerks = len(clerks_salary)
total_managers = len(managers_salary)
total_employees = total_workers + total_clerks + total_managers

total_payroll = sum(workers_salary) + sum(clerks_salary) + sum(managers_salary)

print("Total workers:", total_workers)
print("Total clerks:", total_clerks)
print("Total managers:", total_managers)
print("Total employees:", total_employees)
print("Total payroll:", total_payroll)

print("\nWorker salaries:")
for salary in workers_salary:
    print(salary)

print("\nClerk salaries:")
for salary in clerks_salary:
    print(salary)

print("\nManager salaries:")
for salary in managers_salary:
    print(salary)