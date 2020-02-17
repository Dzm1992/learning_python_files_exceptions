

while True:
	a = input("Podaj pierwszą liczbę ")
	if a == 'q':
		break
	b = input("Podaj drugą liczbę ")
	if b == 'q':
		break
	try:
		answer = int(a) + int(b)
	except ValueError:
		print("Proszę podawać liczby!")
	else:
		print(answer)


