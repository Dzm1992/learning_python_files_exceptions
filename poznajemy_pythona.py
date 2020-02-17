
filename = 'python.txt'


with open(filename) as file_object:
	for line in file_object:
		print(line.strip())
	

		
print("\n")
		
with open(filename) as file_object:
	lines = file_object.readlines()
	
for line in lines:
	print(line.strip())
		

print("\n")

with open(filename) as file_object:
	lines = file_object.read().replace('\n', '')
	print(lines)
