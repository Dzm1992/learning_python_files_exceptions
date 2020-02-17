filenames = ['alice.txt', 'iliad.txt', 'prince.txt']

def fileread(filename):
	"""Odczytuje zawartość plików tekstowych."""
	try:
		with open(filename) as f_object:
			a = f_object.read().count('and')
			print(a)
	except FileNotFoundError:
		print("Nie ma takiego pliku!")
		




for filename in filenames:
	fileread(filename)
