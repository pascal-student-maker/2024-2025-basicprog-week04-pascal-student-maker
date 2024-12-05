#homework 2 solution 
car_a_days = []
car_b_days = []
car_c_days = []

car_a_km = []
car_b_km = []
car_c_km = []

while True:
    car_type = input("Specify the type of car (A, B, C): ").upper()
    if car_type not in ['A', 'B', 'C']:
        print("Invalid car type. Please enter A, B, or C.")
        continue

    days = int(input("Enter the number of days: "))
    km = int(input("Enter the number of kilometers: "))

    if car_type == 'A':
        car_a_days.append(days)
        car_a_km.append(km)
    elif car_type == 'B':
        car_b_days.append(days)
        car_b_km.append(km)
    else:
        car_c_days.append(days)
        car_c_km.append(km)

    more_cars = input("Do you want to enter another car? (yes/no): ")
    if more_cars.lower() != 'yes':
        break

# Calculate totals
total_days_a = sum(car_a_days)
total_days_b = sum(car_b_days)
total_days_c = sum(car_c_days)
total_days = total_days_a + total_days_b + total_days_c

total_km_a = sum(car_a_km)
total_km_b = sum(car_b_km)
total_km_c = sum(car_c_km)
total_km = total_km_a + total_km_b + total_km_c

total_revenue_a = total_days_a * 25 + total_km_a * 0.5
total_revenue_b = total_days_b * 35 + total_km_b * 0.6
total_revenue_c = total_days_c * 45 + total_km_c * 0.7
total_revenue = total_revenue_a + total_revenue_b + total_revenue_c

# Print results
print("Total days:", total_days)
print("Total kilometers:", total_km)
print("Total revenue:", total_revenue)

print("Total days for car A:", total_days_a)
print("Total kilometers for car A:", total_km_a)
print("Total revenue for car A:", total_revenue_a)

print("Total days for car B:", total_days_b)
print("Total kilometers for car B:", total_km_b)
print("Total revenue for car B:", total_revenue_b)

print("Total days for car C:", total_days_c)
print("Total kilometers for car C:", total_km_c)
print("Total revenue for car C:", total_revenue_c)