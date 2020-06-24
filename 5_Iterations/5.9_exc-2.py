"""
Exercise 2: Write another program that prompts for a list of numbers
as above and at the end prints out both the maximum and minimum of
the numbers instead of the average.
"""


l = list(map(int, input("Enter the list of numbers\n").split()))
print (l)

low = None
high = None

for i in l:
    if (low==None or i<=low):
        low = i
    if (high==None or i>=high):
        high = i

print ("Highest number is {0} and Lowest number is {1}".format(high,low))
