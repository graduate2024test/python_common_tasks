from random import random

myList = [2, 4, 5, 9 ,12]

def generate_random_values(number_val):
	for ind in range(number_val):
		yield random()

generator = generate_random_values(5)
for rand_val in generator:
	print(rand_val)
