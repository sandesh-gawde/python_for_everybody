"""
Exercise 2: This program counts the distribution of the hour of the day
for each of the messages. You can pull the hour from the “From” line
by finding the time string and then splitting that string into parts using
the colon character. Once you have accumulated the counts for each
hour, print out the counts, one per line, sorted by hour as shown below.
python timeofday.py

From rjlowe@iupui.edu Fri Jan  4 14:50:18 2008

Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""


file_name = input("Enter file name: ")

try:
    fhand = open(file_name)
except:
    print ("ERROR: File not found")
    exit()

out_dict = dict()
out_list = list()

for line in fhand:
    if "From" in line:
        words = line.split()
        try:
            hour = words[5].split(":")
            out_dict[hour[0]] = out_dict.get(hour[0],0) + 1
        except:
            continue

for k,v in out_dict.items():
    out_list.append((k,v))

out_list.sort()

for k,v in out_list:
    print(k,v)


"""
OUTPUT:
PS C:\Users\Sandesh Gawde\github\sandesh-gawde\python_for_everybody\Chapter_10> python3 .\exc_2.py
Enter file name: C:\Users\Sandesh Gawde\github\sandesh-gawde\python_for_everybody\Chapter_7\mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""
