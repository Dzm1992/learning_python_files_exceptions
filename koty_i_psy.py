filenames = ['dogs.txt', 'cats.txt']

def fileread(filename):
	"""Odczytuje zawartość plików tekstowych."""
	for filename in filenames:
		with open(filename) as f_object:
			a = f_object.read()
			print(a + "\n")


try:
	fileread(filenames)
except FileNotFoundError:
	print("Brakuje pliku!")
