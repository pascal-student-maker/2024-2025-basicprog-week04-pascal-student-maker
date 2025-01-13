type_of_car_a = []
type_of_car_b = []
type_of_car_c = []
days_car_a = []
days_car_b = []
days_car_c = []
number_of_kilometers_car_a = []
number_of_kilometers_car_b = []
number_of_kilometers_car_c = []
def rental_company(type_of_car:str,days_car:int,number_of_kilometers:float):
    if type_of_car =="A":
        days_car_a.append(days_car)
        number_of_kilometers_car_a.append(number_of_kilometers)
    elif type_of_car =="B":
        days_car_b.append(days_car)
        number_of_kilometers_car_b.append(number_of_kilometers)     

    elif type_of_car == "C":
        days_car_c.append(days_car)
        number_of_kilometers_car_c.append(number_of_kilometers)
    else:
        return ValueError(" Wrong type of car try again")
    
number_of_cars = int(input(" Enter  Number of cars rented:"))

for _ in range(number_of_cars):
    type_of_car = input("Enter the  type of car you have rented:")
    days_car = int(input('Enter the amount of days you have driven the car:'))
    number_of_kilometers = float(input("Enter the number of kilometers you have driven:"))
    rental_company(type_of_car,days_car,number_of_kilometers)


revenue_a = sum(days_car_a) * 25 + sum(number_of_kilometers_car_a) * 0.5
revenue_b = sum(days_car_b) * 35 + sum(number_of_kilometers_car_b) * 0.6
revenue_c = sum(days_car_c) * 45 + sum(number_of_kilometers_car_c) * 0.7
total_revenue = revenue_a + revenue_b + revenue_c

print(f" The total number of kilometers driven with car a: {sum(number_of_kilometers_car_a)} ")
print(f" The total number of kilometers driven with car b: {sum(number_of_kilometers_car_b)} ")   
print(f" The total number of kilometers driven with car c: {sum(number_of_kilometers_car_c)} ")  
print(f" The  total days driven with car a: {len(days_car_a)} ") 
print(f" The total days driven with car b : {len(days_car_b)} ") 
print(f" The total days driven with car c: {len(days_car_c)}")
print(f" Revenue of car a : euro {revenue_a} ")
print(f" Revenue of car b : euro {revenue_b} ")
print(f" Revenue of car c : euro  {revenue_c} ")
print(f" Total revenue:  euro {total_revenue:.2f} ")