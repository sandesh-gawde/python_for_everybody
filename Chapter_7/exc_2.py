"""
Exercise 2: Write a program to prompt for a file name, and then read
through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with “X-DSPAM-Confidence:”
pull apart the line to extract the floating-point number on the line.
Count these lines and then compute the total of the spam confidence
values from these lines. When you reach the end of the file, print out
the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
Test your file on the mbox.txt and mbox-short.txt files.
"""

file_name = input("Enter the file name: ")
total = 0.0
count = 0
try:
    file_spam_count = open(file_name)
    print ("File opened successfully\n")
except:
    print ("File not found\nTry using full path of the file")
    exit()


for line in file_spam_count:
    #print ("Entered For loop")
    #print (line)
    if "X-DSPAM-Confidence:" in line:
        #print ("--------------This is valid------------")
        start_index = line.find(": ")+2
        #print ("*****LINE CONFIDENCE*****",line[start_index:])
        try:
            #print ("***SPAM confidence***", line[start_index:])
            spam_confidence = float(line[start_index:])
            #print ("spam_confidence",spam_confidence)
            total += spam_confidence
            count += 1
        except:
            print ("DSPAM confidence level is invalid for line")
            continue


try:
    avg = total/count
    print ("The spam confidence total is {0} and the average is {1}".format(total, avg))
except:
    print ("No DSPAM found")
