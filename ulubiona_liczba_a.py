import json

filename = 'ulubiona_liczba.json'

with open(filename, 'w') as f_object:
	name = input("Podaj swoja ulubioną liczbę ")
	json.dump(name, f_object)
