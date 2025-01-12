#ex17 oplossing

import random

def choose_5_numbers(min_value, max_value):
  new_list = random.sample(range(min_value,max_value+1),5)
  return new_list


min_value = int(input("Enter the minimum:"))
max_value = int(input('Enter the maximum:'))


if max_value - min_value+ 1 < 5:
  print(" range is to little for 5 numbers:")
else:
  print(f" The five selected numbers in between are:  {choose_5_numbers(min_value,max_value)}")  
  
  
  