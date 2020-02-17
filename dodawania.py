a = input("Podaj pierwszą liczbę ")
b = input("Podaj drugą liczbę ")
	
try:
	answer = int(a) + int(b)
except ValueError:
	print("Proszę podawać liczby!")
else:
	print(answer)


