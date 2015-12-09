import sys

if len(sys.argv) == 2:
	filename = sys.argv[1] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as myfile:
    data=myfile.read().replace('\n', '')
	
print data
directions = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)};
currentHouse = {'x': 0, 'y': 0}
houseDeliveries = {}
numHouses = 1

def moveHouses(currentHouse, (x, y)):
	currentHouse['x'] += x
	currentHouse['y'] += y
	return currentHouse


	
for i in range(0, len(data)):
	currentHouse = moveHouses(currentHouse, directions[data[i]])
	print data[i] + " " + str(currentHouse)
	houseString = str(currentHouse['x']) + "x" + str(currentHouse['y'])
	if houseString in houseDeliveries:
		houseDeliveries[houseString] += 1
	else:
		numHouses += 1
		houseDeliveries[houseString] = 1
	
print houseDeliveries
print numHouses

