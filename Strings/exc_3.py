"""
Exercise 3: Encapsulate this code in a function named count, and gen-
eralize it so that it accepts the string and the letter as arguments.
"""

def count(s,a):
    i = 0
    for z in s:
        if (z == a):
            i += 1
    return (i)

inp_str = input("Enter a string: ")
inp_ltr = input("Enter a letter to count: ")

print (count(inp_str, inp_ltr))
