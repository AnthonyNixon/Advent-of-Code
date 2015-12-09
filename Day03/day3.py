import sys

if len(sys.argv) == 2:
	filename = sys.argv[1] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as myfile:
    data=myfile.read().replace('\n', '')
	
print data
directions = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)};
currentHouse = {'santa': {'x': 0, 'y': 0}, 'robo': {'x': 0, 'y': 0}}
houseDeliveries = {'0x0': 1}
numHouses = 1
santasHouse = True

def moveHouses(currentHouse, (x, y)):
	currentHouse['x'] += x
	currentHouse['y'] += y
	return currentHouse


	
for i in range(0, len(data)):
	if santasHouse:
		deliverer = 'santa'
	else:
		deliverer = 'robo'
		
	currentHouse[deliverer] = moveHouses(currentHouse[deliverer], directions[data[i]])
	print deliverer + "\t" + data[i] + " " + str(currentHouse[deliverer]),
	houseString = str(currentHouse[deliverer]['x']) + "x" + str(currentHouse[deliverer]['y'])
	if houseString in houseDeliveries:
		houseDeliveries[houseString] += 1
	else:
		numHouses += 1
		houseDeliveries[houseString] = 1
	print numHouses
	santasHouse = not santasHouse
print houseDeliveries
print numHouses

