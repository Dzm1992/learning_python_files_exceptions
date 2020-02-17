
file_name = 'guest.txt'

with open(file_name, 'w') as file_object:
	x = input("Podaj swoje imię: ")
	file_object.write(x)
	
