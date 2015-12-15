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

ingredients = {}
currentlyAdded = {}
characteristics = ['flavor', 'capacity', 'texture', 'durability']
currentScore = 0
bestForCharacteristic = {}

for line in content:
    matchObj = re.match(r'(.+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)
    ingredient = matchObj.group(1)
    capacity = int(matchObj.group(2))
    durability = int(matchObj.group(3))
    flavor = int(matchObj.group(4))
    texture = int(matchObj.group(5))
    calories = int(matchObj.group(6))

    ingredients[ingredient] = {}
    currentlyAdded[ingredient] = 0

    ingredients[ingredient]['capacity'] = capacity
    ingredients[ingredient]['durability'] = durability
    ingredients[ingredient]['flavor'] = flavor
    ingredients[ingredient]['texture'] = texture
    ingredients[ingredient]['calories'] = calories

for key in ingredients:
    print key + ": " + str(ingredients[key])

def sumCharacteristic(characteristic):
    scores = []
    # print currentlyAdded
    for ingredient in ingredients:
        score = ingredients[ingredient][characteristic]
        score *= currentlyAdded[ingredient]
        scores.append(score)
    # print characteristic + ": " + str(scores) + " = " + str(sum(scores))
    return sum(scores)

def calcScore(info):
    product = 1
    for key in info:
        if info[key] < 0: info[key] = 0
        product *= info[key]
    return product

def getListOfScores(ingredient):
    returnList = []
    for characteristic in characteristics:
        returnList.append(sumCharacteristic(characteristic))

bestScore = 0
for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            for l in range(1, 101):
                if i + j + k + l == 100:
                    currentlyAdded = {'Sugar': i, 'Sprinkles': j, 'Candy': k, 'Chocolate': l}

                    info = {
                        'capacity': sumCharacteristic('capacity'),
                        'durability': sumCharacteristic('durability'),
                        'flavor': sumCharacteristic('flavor'),
                        'texture': sumCharacteristic('texture'),
                    }
                    calories = sumCharacteristic('calories')
                    score = calcScore(info)
                    if calories == 500:

                        if score > bestScore:
                            print info
                            print currentlyAdded
                            print score
                            print
                            bestScore = score
print bestScore


# Algorithm:
#
# Start by determining the best element (best score) to be added first
# try this 99 more times until all 100 TB have been placed
#
# for each iteration, determine which would be best to add
# work off of the best one each iteration.
# Sugar: capacity 3, durability 0, flavor 0, texture -3, calories 2
# Sprinkles: capacity -3, durability 3, flavor 0, texture 0, calories 9
# Candy: capacity -1, durability 0, flavor 4, texture 0, calories 1
# Chocolate: capacity 0, durability 0, flavor -2, texture 2, calories 8
