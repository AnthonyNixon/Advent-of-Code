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

def OR(var1, var2):
	return (var1 | var2)

def AND(var1, var2):
	return (var1 & var2)

def ASSIGN(variable):
	return variable

def LSHIFT(value, amount):
	return (value << amount)

def RSHIFT(value, amount):
	return (value >> amount)

def NOT(value):
	return ~value


operators = {'OR': OR, 'AND': AND, 'ASSIGN': ASSIGN, 'LSHIFT': LSHIFT, 'RSHIFT': RSHIFT, 'NOT': NOT}
wireValues = {}

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def RepresentsVariable(varKey):
	if varKey in wireValues:
		return True
	else:
		return False


def allEvaluated():
	for key in wireValues:
		if not wireValues[key]['evaluated']:
			return False
	return True


def evaluate(varKey):
	print
	variable = wireValues[varKey]
	print variable
	if RepresentsInt(variable['statement']):
		wireValues[varKey]['value'] = int(variable['statement'])
		wireValues[varKey]['evaluated'] = True
	else:
		matchObj = {}
		matchObj = re.match(r'(\S+)\s?(\S+)?\s?(\S+)?', variable['statement'])
		first = matchObj.group(1)
		second = matchObj.group(2)
		third = matchObj.group(3)

		variable1 = ""
		variable2 = ""
		operator = ""

		binaryOperator = False
		unaryOperator = False

		if RepresentsVariable(first):
			variable1 = first
			unaryOperator = True
		elif RepresentsInt(first):
			variable1 = first
		else:
			operator = first

		if RepresentsVariable(second):
			variable1 = second
			unaryOperator = True
		elif second:
			operator = second
		else:
			operator = "ASSIGN"

		if third:
			variable2 = third
			binaryOperator = True
			unaryOperator = False

		print "operator: " + operator + " type: " + str({'unary': unaryOperator, 'binary': binaryOperator})


		if binaryOperator:
			print {"var1": (RepresentsInt(variable1), variable1), "var2": (RepresentsInt(variable2), variable2)}
			if not (RepresentsInt(variable1) or RepresentsInt(variable2)):
				if wireValues[variable1]['evaluated'] and wireValues[variable2]['evaluated']:
					wireValues[varKey]['value'] = operators[operator](wireValues[variable1]['value'], wireValues[variable2]['value'])
				else:
					if not wireValues[variable1]['evaluated']:
						evaluate(variable1)
					if not wireValues[variable2]['evaluated']:
						evaluate(variable2)
					wireValues[varKey]['value'] = operators[operator](wireValues[variable1]['value'], wireValues[variable2]['value'])
			else:
				if RepresentsInt(variable1):
					if wireValues[variable2]['evaluated']:
						wireValues[varKey]['value'] = operators[operator]( int(variable1), wireValues[variable2]['value'])
					else:
						evaluate(variable2)
						wireValues[varKey]['value'] = operators[operator]( int(variable1), wireValues[variable2]['value'])
				elif RepresentsInt(variable2):
					if wireValues[variable1]['evaluated']:
						wireValues[varKey]['value'] = operators[operator](wireValues[variable1]['value'], int(variable2))
					else:
						evaluate(variable1)
						wireValues[varKey]['value'] = operators[operator](wireValues[variable1]['value'], int(variable2))
			wireValues[varKey]['evaluated'] = True

		elif unaryOperator:
			if wireValues[variable1]['evaluated']:
				wireValues[varKey]['value'] = operators[operator](wireValues[variable1]['value'])
			else:
				evaluate(variable1)
				wireValues[varKey]['value'] = operators[operator](wireValues[variable1]['value'])
			wireValues[varKey]['evaluated'] = True

for i in range(0, len(content)):
	line = content[i].replace('\n', '').replace('\r', '')

	matchObj = re.match(r'(.+) -> (.+)', line)
	assignStatement = matchObj.group(1)
	variable = matchObj.group(2)

	wireValues[variable] = {'statement': assignStatement, 'value': 0, 'evaluated': False}

print json.dumps(wireValues, indent=2)

while not allEvaluated():
	for key in wireValues:
		evaluate(key)

print json.dumps(wireValues, indent=2)
print wireValues['a']



	# 123 -> x
	# 456 -> y
	# x AND y -> d
	# x OR y -> e
	# x LSHIFT 2 -> f
	# y RSHIFT 2 -> g
	# NOT x -> h
	# NOT y -> i
