#!/usr/bin/env python3

#===========================#
"""
Own example to explain the various types of class methods
Covers all 3 types:
    Classmethod, Staticmethod, Instancemethod.
"""
#===========================#


class gym:

    members = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        gym.newmember(name,age)
        self.log = list()


    @classmethod
    def newmember(cls, name="Admin-Call", age=0):
        cls.members += 1
        print ("New Member:\n\tName: {}\n\tAge: {}\nUpdating cataloge: Total members {}".format(name,age,cls.members))

    @staticmethod
    def offer_assist(age):
        if (age>=60) :
            print ("Assistance avaialbe for elderly member")
        else:
            print ("Member not eligible for elderly assistance")

    #instance_method
    def member_log(self, exe):
        self.exe = exe
        print ("Gym member {} doing exercise: {}".format(self.name,self.exe))
        self.log.append(self.exe)

    #instance_method
    def retrive_log(self):
        print ("Exercise log for member name {}: {}".format(self.name,self.log))


def main():
    m1 = gym("Sam",25)
    print ("Number of gym members: ",gym.members)

    #gym.newmember()
    
    #Random member stopped at frontdesk and asked if elligble for assistance
    gym.offer_assist(37)

    m1.member_log("Crunches")
    m1.retrive_log()
    m1.member_log("Legs day")
    m1.retrive_log()


    m2 = gym("Ria",22)

    #gym.newmember()
    print ("Now how many members: ", gym.members)

    m2.member_log("Cardio")
    m2.retrive_log()
    m1.retrive_log()
    m2.member_log("SuryaNamaskar")
    m2.retrive_log()


if __name__ == "__main__":
    main()
