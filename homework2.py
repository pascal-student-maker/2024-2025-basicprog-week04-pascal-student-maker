


#ex 18 solutin 

kilometers_carA = []
kilometers_carB = []
kilometers_carC= []
x= "km"
carAcost =  0.5
carBcost =   0.6
carCcost =   0.7

while True:
    car_type = input("Specify the type of Car (A: Car A, B: Car B, C: Car C): ")
    if car_type.upper() not in ['A', 'B', 'C']:
        print("Invalid employee type. Please enter A, B, or C.")
        continue

    days = int(input("Enter the days: "))

    if days_type.upper() == 'A':
        days_type.append(days)
    elif days_type.upper() == 'B':
        days_type.append(days)
    else:
        days_type.append(days)

    more_days = input("Do you want to enter another day? (yes/no): ")
    if more_days.lower() != 'yes':
        break

# Calculate totals and print results
total_revenue_CarA = total_days_carA + carAcost * kilometers_carA + 25
total_revenue_CarB = total_days_carB + carBcost * kilometers_carB + 35
total_revenue_CarC = total_days_carC + carCcost * kilometers_carC + 45
total_days_carA = len(days_type)
total_days_carB = len(days_type)
total_days_carC = len(days_type)
total_days = total_days_carA + total_days_carB + total_days_carC

total_car_cost = sum(carAcost) + sum(carBcost) + sum(carCcost)
total_car_kilometers = sum(kilometers_carA ) + sum(kilometers_carB ) + sum(kilometers_carC)
total_revenue = sum(total_revenue_CarA) + sum(total_revenue_CarB) + sum(total_revenue_CarC)

print("Total days:", total_days)
print("Total car cost:", total_car_cost)
print("Total Kilometers:", total_car_kilometers)
print("Total revenue :", total_revenu)
print("Total days car a :", total_days_carA)
print("Total days car b :", total_days_carB)
print("Total days car c :", total_days_carC)
print(" Total kilometers car a:", kilometers_carA)
print("Total kilometers car b:", kilometers_carB)
print("Total kilometers car c:", kilometers_carC)
print("Total revenue car a:",total_revenue_CarA)
print("Total revenue car b:", total_revenue_CarB)
print("Total revenue car c:", total_revenue_CarC)


