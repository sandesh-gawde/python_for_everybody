#!/usr/bin/python3
#Class variables vs Object variables.
#Class variables: Available to all methods of the class
#Object variables: Unique to object, independent for each instance

class Robot:
    robo_population = 0         #class variable

    def count_robo(self):
        print (Robot.robo_population)

    def __init__(self, name):
        self.name = name
        print ("Hi,",self.name," is a new Robo")
        Robot.robo_population += 1      #new Robo added
        Robot.count_robo(self)

    #@classmethod


    def kill_robo(self, name):
        self.name = name
        print (self.name," got killed")
        Robot.robo_population -= 1       #remove one Robo
        Robot.count_robo(self)

    def greet_robo(self):
        print ("Greeting all of our ",Robot.robo_population," Robos")
        Robot.count_robo(self)

    @classmethod
    def call_robo(cls):
        print ("In class method ",cls.robo_population)


r = Robot("Zach")
r.count_robo()
s = Robot("Su")
r.count_robo()
s.count_robo()
r.greet_robo()
r.kill_robo("Zach")
r.call_robo()
