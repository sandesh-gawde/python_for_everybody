Often, we want to look into a string and find a substring. For example if we were
presented a series of lines formatted as follows:
From stephen.marquard@ uct.ac.za Sat Jan 5 09:14:16 2008
and we wanted to pull out only the second half of the address (i.e., uct.ac.za)
from each line, we can do this by using the find method and string slicing.
First, we will find the position of the at-sign in the string. Then we will find the
position of the first space after the at-sign. And then we will use string slicing to
extract the portion of the string which we are looking for.
>>> data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
>>> atpos = data.find('@')
>>> print(atpos)
21
>>> sppos = data.find(' ',atpos)
>>> print(sppos)
31
>>> host = data[atpos+1:sppos]
>>> print(
