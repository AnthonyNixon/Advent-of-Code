import sys
import itertools
import re

if len(sys.argv) == 2:
	filename = sys.argv[1] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as f:
    content = f.readlines()


lights = [[0 for x in range(1000)] for x in range(1000)]

def initialize():
	for i in range(0, 1000):
		for j in range(0, 1000):
			lights[i][j] = 0


def off(fromX, fromY, toX, toY, version):
	if version == 1:
		for x in range(fromX, toX + 1):
			for y in range(fromY, toY + 1):
				lights[x][y] = 0
	elif version == 2:
		for x in range(fromX, toX + 1):
			for y in range(fromY, toY + 1):
				lights[x][y] -= 1
				if lights[x][y] < 0:
					lights[x][y] = 0
def on(fromX, fromY, toX, toY, version):
	if version == 1:
		for x in range(fromX, toX + 1):
			for y in range(fromY, toY + 1):
				lights[x][y] = 1
	elif version == 2:
		for x in range(fromX, toX + 1):
			for y in range(fromY, toY + 1):
				lights[x][y] += 1
def toggle(fromX, fromY, toX, toY, version):
	if version == 1:
		for x in range(fromX, toX + 1):
			for y in range(fromY, toY + 1):
				if lights[x][y] == 1:
					lights[x][y] = 0
				elif lights[x][y] == 0:
					lights[x][y] = 1
	elif version == 2:
		for x in range(fromX, toX + 1):
			for y in range(fromY, toY + 1):
				lights[x][y] += 2

def countLights(version):
	if version == 1:
		numLights = {'on': 0, 'off': 0}
		for x in range(0, 1000):
			for y in range(0, 1000):
				if lights[x][y] == 1:
					numLights['on'] += 1
				else:
					numLights['off'] += 1
		return numLights
	elif version == 2:
		totalBrightness = 0
		for x in range(0, 1000):
			for y in range(0, 1000):
				totalBrightness += lights[x][y]
		return totalBrightness

for version in [1, 2]:
	print version
	initialize()
	for i in range(0, len(content)):
		line = content[i].replace('\n', '').replace('\r', '')
		matchObj = re.match(r'(.+) (\d+),(\d+) through (\d+),(\d+)', line)
		#print line

		fromX = int(matchObj.group(2))
		fromY = int(matchObj.group(3))
		toX = int(matchObj.group(4))
		toY = int(matchObj.group(5))

		operation = matchObj.group(1)
		if operation.lower() == 'turn off':
			off(fromX, fromY, toX, toY, version)
		elif operation.lower() == 'turn on':
			on(fromX, fromY, toX, toY, version)
		elif operation.lower() == 'toggle':
			toggle(fromX, fromY, toX, toY, version)

	print countLights(version)
