"""
Exercise 5: This program records the domain name (instead of the
address) where the message was sent from instead of who the mail came
from (i.e., the whole email address). At the end of the program, print
out the contents of your dictionary.
python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""


file_name = input("Enter file name: ")
try:
    file_h = open(file_name)
except:
    print ("File not found, please try entering complete path")
    exit()

domain = {}

for line in file_h:
    if "From" in line:
        words = line.split()
        if len(words)>2:
            domain[(words[1].split('@'))[1]] = domain.get((words[1].split('@'))[1],0) +1

print (domain)


"""
Output:
PS C:\Users\Sandesh Gawde\github\sandesh-gawde\python_for_everybody\Chapter_9> python3 .\exc_5.py
Enter file name: C:\Users\Sandesh Gawde\github\sandesh-gawde\python_for_everybody\Chapter_7\mbox-short.txt
{'uct.ac.za': 6, 'media.berkeley.edu': 4, 'umich.edu': 7, 'iupui.edu': 8, 'caret.cam.ac.uk': 1, 'gmail.com': 1}
"""
