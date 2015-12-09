with open ("input.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')
	
print data
floor = 0
count = 1
firstBasement = 0

for i in range(0, len(data)):
	print data[i],
	if (data[i] == '('):
		floor+=1
	elif (data[i] == ')'):
		floor-=1
	print floor
	if (floor < 0):
		if (firstBasement == 0):
			firstBasement = count
	count+=1

print firstBasement