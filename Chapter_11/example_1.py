# Search for lines that contain 'From'

import re

try:
    fhand = open("C:\\Users\\Sandesh Gawde\\github\\sandesh-gawde\\python_for_everybody\\Chapter_7\\mbox-short.txt")
except:
    print ("ERROR: File not found")
    exit()

for line in fhand:
    if re.search("From:",line):
        print (line)
