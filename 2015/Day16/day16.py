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

ticker = {
    'children': {'num': 3, 'type': 'eq'},
    'cats': {'num': 7, 'type': 'gt'},
    'samoyeds': {'num': 2, 'type': 'eq'},
    'pomeranians': {'num': 3, 'type': 'lt'},
    'akitas': {'num': 0, 'type': 'eq'},
    'vizslas': {'num': 0, 'type': 'eq'},
    'goldfish': {'num': 5, 'type': 'lt'},
    'trees': {'num': 3, 'type': 'gt'},
    'cars': {'num': 2, 'type': 'eq'},
    'perfumes': {'num': 1, 'type': 'eq'}
}

def sueMatchesTicker(sue):
    for num in sue:
        sueMatch = True
        for quality in sue[num]:
            if ticker[quality]['type'] == 'gt':
                if sue[num][quality] <= ticker[quality]['num']:
                    return False
            elif ticker[quality]['type'] == 'lt':
                if sue[num][quality] >= ticker[quality]['num']:
                    return False
            else:
                if sue[num][quality] != ticker[quality]['num']:
                    return False
        print
        return True


sues = []
for line in content:
    matchObj = re.match(r'Sue (\d+): (.+): (\d+), (.+): (\d+), (.+): (\d+)', line)
    sue = {matchObj.group(1): {
                                matchObj.group(2): int(matchObj.group(3)),
                                matchObj.group(4): int(matchObj.group(5)),
                                matchObj.group(6): int(matchObj.group(7))
                            }
        }
    sues.append(sue)

matches = []
for sue in sues:
    print sue
    if sueMatchesTicker(sue):
        matches.append(sue)

print "Matches: \n" + str(matches)
