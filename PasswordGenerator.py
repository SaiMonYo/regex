import re

passwords = []

f = open("passwords.txt","r")

for line in f:
    passwords.append(line.strip())

f.close()

c = 0
for p in passwords:
    #alternating letter digit
    if re.match("[A-Z][0-9][A-Z][0-9][A-Z][0-9]",p):
        c += 1
        print(p)


