import hashlib

# Read in the input file.
with open ("input.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

n = 0

for i in range(8): # Finding 8 character password
    valid = False
    while not valid:
        currentInput = data + str(n)
        hashed = hashlib.md5(currentInput).hexdigest()
        if hashed[:5] == '00000':
            valid = True
            print "'" + currentInput + "'\t==> " + hashed[5] + " " + hashed + " " + str(n)
        
        n += 1
