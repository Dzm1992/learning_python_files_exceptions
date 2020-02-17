import json

filename = 'ulubiona_liczba.json'

with open(filename) as f_object:
	your_name = json.load(f_object)
	print ("Witaj z powrotem! Twoja ulubiona liczba to: " + your_name + "!")
