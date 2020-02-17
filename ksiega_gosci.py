
filename = 'guest_book.txt'
x = ''


with open(filename, 'a') as file_object:
	while True:
		x = input("Podaj swoje imię: ")
		if x == 'q':
			break
		else:
			print("Witaj " + x + "!")
			file_object.write("\n")
			file_object.write(x)
		
