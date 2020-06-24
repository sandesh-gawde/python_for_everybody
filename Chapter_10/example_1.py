"""
For example, suppose you have a list of words and you want to sort them from
longest to shortest:
txt = 'but soft what light in yonder window breaks'
"""

txt = 'but soft what light in yonder window breaks'
word_list = txt.split()

out_list = list()
for word in word_list:
    out_list.append((len(word),word))
out_list.sort(reverse=True)

[print (n,end=" ") for m,n in out_list]
