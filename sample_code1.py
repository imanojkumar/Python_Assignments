import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print line

print ("file name: mbox-short.txt")
option1 = raw_input("Enter another file [mbox.txt]: ")

hand = open(option1)
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print line
