"""
Exercise 1: Write a simple program to simulate the operation of the
grep command on Unix. Ask the user to enter a regular expression and
count the number of lines that matched the regular expression:
$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author
$ python grep.py
Enter a regular expression: ^Xmbox.
txt had 14368 lines that matched ^X-
$ python grep.py
Enter a regular expression: java$
mbox.txt had 4175 lines that matched java$
"""


from re import *

pattern = compile(input("Enter a patter to find: "))

try:
    fhand = open(r"C:\Users\Sandesh Gawde\github\sandesh-gawde\python_for_everybody\Chapter_7\mbox-short.txt")
except:
    print ("File not found, please enter full path")
    exit()

count = 0

for line in fhand:
    line = line.rstrip()
    if search(pattern, line):
        count += 1

print (count)
