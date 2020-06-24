
"""
Exercise 1: Write a program which repeatedly reads numbers until the
user enters “done”. Once “done” is entered, print out the total, count,
and average of the numbers. If the user enters anything other than a
number, detect their mistake using try and except and print an error
message and skip to the next number.
"""

count = 0
total = 0

while True:
    i = input("Enter a number: ")
    try:
        i = int(i)
        count += 1
        total += i
    except:
        if (i == "done"):
            break
        else:
            print ("Enter valid data")
            continue

print (total, count, total/count)
