import re

# Read in the input file.
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()

def get_abas(word):
    abas = []
    for i in range(0, len(word) - 2):
        slc = word[i:i+3]
        if slc[0] == slc[2] and slc[0] != slc[1]:
            abas.append(slc)
    return abas

def isTLS(ipaddress):
    match = re.search(r'\[[^\]]*(\w)(\w)\2\1.*\]', ipaddress)
    if ((match is not None) and not (match.group(1) == match.group(2))):
        return False

    match = re.search(r'(\w)(\w)\2\1', ipaddress)
    return ((match is not None) and not (match.group(1) == match.group(2)))

def isSSL(ipaddress):
    regex = re.compile('.*\[([a-z]+)\].*')
    hypernets = []
    while True:
        m = regex.match(ipaddress)
        if not m:
            break
        inner = m.groups()[0]
        hypernets.append(inner)
        ipaddress = ipaddress.replace(inner, '')
    abas = get_abas(ipaddress)
    for a in abas:
        bab = ''.join( [ a[1], a[0], a[1] ] )
        for h in hypernets:
            if bab in h:
                return True
    return False

tls_count = 0
ssl_count = 0
for line in data:
    if isTLS(line):
        tls_count += 1
    if isSSL(line):
        ssl_count += 1

print "tls: " + str(tls_count)
print "ssl: " + str(ssl_count)
