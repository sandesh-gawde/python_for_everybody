#!/usr/bin/python3
class PartyAnimal:
   x = 0
    #name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self) :
        self.x = self.x + 1
        print(self.name,'party count',self.x)

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')
s.party()
j.party()
s.party()

#====== output ======
"""
13:56 $ ./example_14_9.py
Sally constructed
Jim constructed
Sally party count 1
Jim party count 1
Sally party count 2
"""
