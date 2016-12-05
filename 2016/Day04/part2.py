import re
import string

# Read in the input file.
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()

def caesar(plaintext, shift):
    while shift > 26:
        shift -= 26
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

for line in data:
    print line
    matchGroup = re.match('(.+?)-(\d+?)\[(.+?)\]', line)
    letters = matchGroup.group(1)
    numbers = int(matchGroup.group(2))
    checksum = matchGroup.group(3)

    print "letters: " + letters
    print "numbers: " + str(numbers)
    print "checksum: " + checksum
    roomName = caesar(letters, numbers)

    if "north" in roomName:
        print numbers
        break
