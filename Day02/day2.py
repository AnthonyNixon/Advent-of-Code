with open("input.txt") as f:
    content = f.readlines()
	
for i in range(0, len(content)):
	print str(i) + " - " + content[i]
	parts = 