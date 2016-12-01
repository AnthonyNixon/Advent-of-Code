import sys
import itertools
import re

if len(sys.argv) == 2:
	filename = sys.argv[1] + ".txt"
else:
	filename = "input.txt"

with open (filename, "r") as f:
    content = f.readlines()

for part in [2]:
	if part == 1:
		sizes = []
		totalCodeLen = 0
		totalCharCount = 0
		for i in range(0, len(content)):
			line = str(content[i].rstrip('\r\n'))

			print line + ": " + str(len(line))

			def evalString(string):
				i = 0
				while i < (len(string) - 1):
					if string[i] == '\\':
						if string[i+1] == '\\':
							print string[i:i+2]
							string = string[:i] + '.' + string[i+2:]
							i = 0
						elif string[i+1] == '\"':
							print string[i:i+2]
							string = string[:i] + '.' + string[i+2:]
							i = 0
						elif string[i+1] == 'x':
							print string[i:i+4]
							string = string[:i] + '.' + string[i+4:]
							i = 0
					i += 1
				return string[1:-1]

			parsedString = evalString(line)
			print parsedString
			print
			sizes.append({'codeLen': len(line), 'charCount': len(parsedString)})
			totalCodeLen += len(line)
			totalCharCount += len(parsedString)

		print sizes
		print str(totalCodeLen - totalCharCount)
	elif part == 2:
		sizes = []
		totalCodeLen = 0
		totalCharCount = 0
		for i in range(0, len(content)):
			line = str(content[i].rstrip('\r\n'))

			print line + ": " + str(len(line))

			def evalString(string):
				i = 0
				string = string[1:-1]
				string = string.replace('\\', '/')
				string = string.replace('/', '<SLASH>')
				string = string.replace('"', '<QUOTE>')
				string = string.replace('/x', '<CHAR>')

				string = string.replace('<SLASH>', '//')
				string = string.replace('<QUOTE>', '/"')
				string = string.replace('<CHAR>', '//x')
				# while i < (len(string) - 2):
				# 	if string[i] == '"':
				# 		string = string[:i] + '/"' + string[i:]
				# 		i += 2
				# 	if string[i] == '\\':
				# 		if string[i+1] == 'x':
				# 			string = string[:i] + '//x' + string[i+2:]
				# 			i += 2
				# 		else:
				# 			string = string[:i] + '//' + string[i+1:]
				# 			i += 2
				# 	i += 1
				#
				return '"/"' + string + '/""'

			parsedString = evalString(line)
			print parsedString,
			sizes.append({'codeLen': len(line), 'charCount': len(parsedString)})
			totalCodeLen += len(line)
			totalCharCount += len(parsedString)
			print " " + str(len(parsedString))
			print

		print sizes
		print str(totalCharCount - totalCodeLen)
