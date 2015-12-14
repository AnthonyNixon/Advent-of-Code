import sys
import itertools
import re
import json


simSeconds = 0
if len(sys.argv) == 2:
	simSeconds = int(sys.argv[1])
	filename = "input.txt"

elif len(sys.argv) == 3:
	simSeconds = int(sys.argv[1])
	filename = sys.argv[2] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as f:
    content = f.readlines()

reindeer = {}

for line in content:
	matchObj = re.match(r'(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+)', line)
	deer = matchObj.group(1)
	speed = matchObj.group(2)
	flyTime = matchObj.group(3)
	restTime = matchObj.group(4)

	reindeer[deer] = {}
	reindeer[deer]['speed'] = int(speed)
	reindeer[deer]['flyTime'] = int(flyTime)
	reindeer[deer]['restTime'] = int(restTime)
	reindeer[deer]['distance'] = 0
	reindeer[deer]['restingAtTime'] = 0
	reindeer[deer]['state'] = {'currently': 'flying', 'since': 0}
	reindeer[deer]['winPoints'] = 0

def printReindeer():
	for deer in reindeer:
		print reindeer[deer]
		print

def printWinner(version):
	if version == 'v1':
		maxDist = 0
		winner = ''
		for deer in reindeer:
			if reindeer[deer]['distance'] > maxDist:
				maxDist = reindeer[deer]['distance']
				winner = deer
		print winner + " won at distance of " + str(maxDist)
	elif version == 'v2':
		maxPoints = 0
		winner = ''
		for deer in reindeer:
			if reindeer[deer]['winPoints'] > maxPoints:
				maxPoints = reindeer[deer]['winPoints']
				winner = deer
		print winner + " won with " + str(maxPoints) + " points"

def getCurrentLeaders():
	maxDist = 0
	leaders = []
	for deer in reindeer:
		if reindeer[deer]['distance'] > maxDist:
			maxDist = reindeer[deer]['distance']
	for deer in reindeer:
		if reindeer[deer]['distance'] == maxDist:
			leaders.append(deer)
	return leaders



def simulateDeer(deer, time):
	deer = reindeer[deer]
	if deer['state']['currently'] == 'flying':
		deer['distance'] += int(deer['speed'])
		if time - deer['state']['since'] == deer['flyTime']:
			deer['state'] = {'currently': 'resting', 'since': time}
	elif deer['state']['currently'] == 'resting':
		if time - deer['state']['since'] == deer['restTime']:
			deer['state'] = {'currently': 'flying', 'since': time}

def simulateRace(time):
	currentTime = 1
	while currentTime <= time:
		print "Time = " + str(currentTime)
		for deer in reindeer:
			simulateDeer(deer, currentTime)
		for deer in getCurrentLeaders():
			reindeer[deer]['winPoints'] += 1
		currentTime += 1
	printReindeer()
	printWinner('v1')
	printWinner('v2')


simulateRace(simSeconds)
