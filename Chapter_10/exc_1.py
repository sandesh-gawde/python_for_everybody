"""
Exercise 1: Revise a previous program as follows: Read and parse the
“From” lines and pull out the addresses from the line. Count the num-
ber of messages from each person using a dictionary.
After all the data has been read, print the person with the most commits
by creating a list of (count, email) tuples from the dictionary. Then
sort the list in reverse order and print out the person who has the most
commits.
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
"""

file_name = input ("Enter the file name: ")

try:
    fhand = open(file_name)
except:
    print ("ERROR: File not found")
    exit()

out_dict = dict()

for line in fhand:
    if "From" in line:
        words = line.split()
        if (len(words)>2):
            out_dict[words[1]] = out_dict.get(words[1],0) + 1

out_list = list()

#print (out_dict.items())


for key,value in out_dict.items():
    out_list.append((value,key))

out_list.sort(reverse=True)

highest_count = out_list[0][0]

for v,k in out_list:
    if (v==highest_count):
        print (k,v)
