# -*- coding: utf-8 -*-
"""
Created on Sun May 20 17:13:59 2018

@author: jaredalbert
"""



class Base:
    numOfInstances = 0
    def __init__(self, name = 'nomani'):
        Base.numOfInstances += 1
    def getNumInstances(self):
        print ('number of instances: ', self.numOfInstances)
	    
b1 = Base()

# It should print 1
b2 = Base()
b1.getNumInstances()
# It should print 2
b2.getNumInstances()

b1.getNumInstances()
b3 = Base()
#It should print 2

b1.getNumInstances()