"""
Exercise 3: Write a program to read through a mail log, build a his-
togram using a dictionary to count how many messages have come from
each email address, and print the dictionary.
Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dic-
tionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
"""

file_name = input("Enter file name: ")

try:
    file_h = open(file_name)
except:
    print ("Incorrect file")
    exit()

mail_box = {}

for line in file_h:
    if "From" in line:
        words = line.split()
        #print (words, len(words))
        if len(words)>2:
            try:
                mail_box[words[1]] = mail_box.get(words[1],0) + 1
            except:
                continue
#print (mail_box)

highest_sender = None
highest_count = None

for sender in mail_box:
    if (highest_count is None) or (mail_box[sender]>highest_count):
        highest_count = mail_box[sender]
        highest_sender = sender

print (highest_sender, highest_count)


"""
PS C:\Users\Sandesh Gawde\github\sandesh-gawde\python_for_everybody\Chapter_9> python3 .\exc_4.py
Enter file name: C:\Users\Sandesh Gawde\github\sandesh-gawde\python_for_everybody\Chapter_7\mbox-short.txt
cwen@iupui.edu 5
"""
