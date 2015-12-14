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

reindeer = {}

for line in content:
    matchObj = re.match(r'(.+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+)', line)
    deer = matchObj.group(1)
    speed = matchObj.group(2)
    flyTime = matchObj.group(3)
    restTime = matchObj.group(4)

    reindeer[deer] = {}
    reindeer[deer]['speed'] = speed
    reindeer[deer]['flyTime'] = flyTime
    reindeer[deer]['restTime'] = restTime
    reindeer[deer]['distance'] = 0
    reindeer[deer]['restingAtTime'] = -1

def simulateDeer(time):
    return 1

def simulateRace(time):
    currentTime = 0
    while currentTime < time:
        for deer in reindeer:
            simulateDeer(currentTime)
        currentTime += 1
    print reindeer


print reindeer
simulateRace(2503)
