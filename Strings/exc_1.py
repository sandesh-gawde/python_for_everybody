"""
Exercise 1: Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards.
"""

s = input("Enter the string\n")

i = (len(s)-1)

while i>=0:
    print (s[i])
    i -= 1
