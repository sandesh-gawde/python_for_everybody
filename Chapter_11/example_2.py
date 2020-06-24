# Search for lines that start with From and have a timestamp
#From stephen.marquard@uct.ac.za Fri Jan  4 04:07:34 2008

import re

fhand = open("C:\\Users\\Sandesh Gawde\\github\\sandesh-gawde\\python_for_everybody\\Chapter_7\\mbox-short.txt")

for line in fhand:
    line = line.rstrip()
    if re.search(r"^From.*\d\d:\d\d:\d\d.*",line):
        print(line)
