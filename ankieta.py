filename = 'ankieta.txt'
x = ''

with open(filename, 'a') as file_object:
	while True:
		x = input("Dlaczego lubisz programowanie? ")
		if x == 'q':
			break
		else:
			file_object.write(x + "\n")
