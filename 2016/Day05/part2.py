import hashlib

# Read in the input file.
with open ("input.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')

n = 0
passwordPieces = {}

while len(passwordPieces) < 8: # Finding 8 character password
    currentInput = data + str(n)
    hashed = hashlib.md5(currentInput).hexdigest()
    if hashed[:5] == '00000':
        char = hashed[6]
        position = hashed[5]
        if position.isdigit() and int(position) < 8 and position not in passwordPieces:
            passwordPieces[position] = char
            print "'" + currentInput + "'\t==> " + char + " @ " + position + " " + hashed
    n += 1

password = []
print passwordPieces
for i in range(8):
    password.append(passwordPieces[str(i)])
print "".join(password)
