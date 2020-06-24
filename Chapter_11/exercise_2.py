"""
Exercise 2: Write a program to look for lines of the form:
New Revision: 39772
Extract the number from each of the lines using a regular expression
and the findall() method. Compute the average of the numbers and
print out the average as an integer.
Enter file:mbox.txt
38549
Enter file:mbox-short.txt
39756
"""

import re

try:
    fhand = open(r"C:\Users\Sandesh Gawde\github\sandesh-gawde\python_for_everybody\Chapter_7\mbox-short.txt")
except:
    print("File not found, try entering full path")
    exit()

count = 0
total = 0
#value = None

for line in fhand:
    line = line.rstrip()
    values = re.findall("New Revision: ([0-9]*)",line)
    if len(values)>0:
        #count += 1
        #print (values)
        for value in values:
            count += 1
            total += int(value)

print(int(total/count))
