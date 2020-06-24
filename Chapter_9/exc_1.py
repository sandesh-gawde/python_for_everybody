"""
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn’t matter what the values are. Then you
can use the in operator as a fast way to check whether a string is in the
dictionary.
"""


file_name = input("Enter the file name: ")

try:
    file_text = open(file_name)
except:
    print ("File doesn't exist")
    exit()

d = dict()

for line in file_text:
    try:
        t = line.split()
        #print ("Debug: ",t)
    except:
        continue
    for word in t:
        #print ("DEBUG word: ", word)
        d[word] = None

print (d)
