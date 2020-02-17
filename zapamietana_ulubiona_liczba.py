import json

filename = 'ulubiona_liczba.json'


try:
	with open(filename) as f_object:
		your_name = json.load(f_object)
except FileNotFoundError:
	with open(filename, 'w') as f_object:
		your_name = input("Podaj swoją ulubioną liczbę: ")
		saved_name = json.dump(your_name, f_object)
		print("Twoje ulubiona liczba została zapisana.")
else:
	print("Witaj ponownie, twoja ulubiona liczba to: " + your_name)
