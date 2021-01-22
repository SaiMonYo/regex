import re

passwords = []

f = open("passwords.txt","r")

for line in f:
    passwords.append(line.strip())

f.close()


for p in passwords:
    if re.match("[A-Z][0-9][A-Z][0-9][A-Z][0-9]",p):
        print(p)


