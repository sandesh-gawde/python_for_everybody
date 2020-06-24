"""
Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the program print
out the contents of your dictionary (order does not matter).
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
Sample Execution:
python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""
file_name = input("Enter the file name: ")
try:
    file_h = open(file_name)
except:
    print ("Incorrect file name")
    #raise
    exit()

out_dict = dict()

for line in file_h:
    if ("From" in line):
        try:
            words = line.split()
            #print(words)
            out_dict[words[2]] = out_dict.get(words[2],0) + 1
        except:
            continue

print (out_dict)


"""
Output:
PS C:\Users\Sandesh Gawde\github\sandesh-gawde\python_for_everybody\Chapter_9> python3 .\exc_2.py
Enter the file name: C:\Users\Sandesh Gawde\github\sandesh-gawde\python_for_everybody\Chapter_7\mbox-short.txt
{'Sat': 1, 'Fri': 20, 'Thu': 6}
"""
