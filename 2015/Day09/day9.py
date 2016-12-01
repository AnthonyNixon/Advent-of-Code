import sys
import itertools
import re
import json

if len(sys.argv) == 2:
	filename = sys.argv[1] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as f:
    content = f.readlines()

def parseLine(line):
	matchObj = re.match(r'(.+) to (.+) = (\d+)', line)
	return ([matchObj.group(1), matchObj.group(2)], matchObj.group(3))

def getDistance():
	return 1

cities = []
distances = {}
for i in range(0, len(content)):
	line = str(content[i].rstrip('\r\n'))

	([fromCity, toCity], distance) = parseLine(line)

	if fromCity not in cities:
		cities.append(fromCity)
	if toCity not in cities:
		cities.append(toCity)
	if fromCity not in distances:
		distances[fromCity] = {}
	if toCity not in distances:
		distances[toCity] = {}

	distances[fromCity][toCity] = distance
	distances[toCity][fromCity] = distance


permutations = list(itertools.permutations(cities))

print cities
print
print distances
print


def calculateTotalDistance(route):
	distance = 0
	for i in range(0, (len(route) - 1)):
		distance += int(distances[route[i]][route[i+1]])
	return distance

def formattedRoute(route):
	cityList = []
	for city in route:
		cityList.append(city)
	return ' -> '.join(cityList)

shortestRoute = {'distance': -1, 'route': []}
longestRoute = {'distance': -1, 'route': []}

for permutation in permutations:
	print permutation
	distance = calculateTotalDistance(permutation)
	if shortestRoute['distance'] == -1 or distance < shortestRoute['distance']:
		shortestRoute = {'distance': distance, 'route': permutation}
	if longestRoute['distance'] == -1 or distance > longestRoute['distance']:
		longestRoute = {'distance': distance, 'route': permutation}

print
print "Shortest Route:"
print formattedRoute(shortestRoute['route']) + " = " + str(shortestRoute['distance'])
print
print "Longest Route:"
print formattedRoute(longestRoute['route']) + " = " + str(longestRoute['distance'])
