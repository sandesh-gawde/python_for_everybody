"""
In the last example, the method lower is called and then we use startswith to
see if the resulting lowercase string starts with the letter “h”. As long as we are
careful with the order, we can make multiple method calls in a single expression.
**Exercise 4: There is a string method called count that is similar to the function
in the previous exercise. Read the documentation of this method at:
https://docs.python.org/library/stdtypes.html#string-methods
Write an invocation that counts the number of times the letter a occurs in “banana”.**

>>> s = "banana"
3
>>> s.count('b')
1
"""

"""
def count_pattern(inp_str,a):
    counter = 0
    for z in inp_str:
        if (z == a):
            counter += 1
    return (counter)

inp_str = input("Enter a string: ")
p = input("Enter a pattern to find: ")

print (count_pattern(inp_str,p))
"""
#function takes stirng and a pattern, returns the number of occurances of pattern in the string
def count_pattern(inp_str,a):
    counter = 0
    l = len(a)
    i = 0           #initialize to 1st char
    j = 0+l         #initialize to 1st-char + lenght of pattern, create window to search
    while (j<=len(inp_str)):
        if (inp_str[i:j]) == a:
            counter += 1
        i += 1
        j += 1
    return (counter)

#take string and pattern as input from user
inp_str = input("Enter a string: ")
p = input("Enter a pattern to find: ")

#call function and print the number of times the pattern is repeated in the string
print (count_pattern(inp_str,p))
