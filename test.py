# -*- coding: utf-8 -*-
"""
Created on Sun May 20 17:30:06 2018

@author: jaredalbert
"""

class Test2:
    num_of_test = 0
    def __init__(self, name):
        Test2.num_of_test +=1
    def num_tests(self):
        print (self.num_of_test)
    def __repr__(self):
        return '{}'.format(name)
        
test_1 = Test2('mia')
print ('name', test_1.__repr__())
test_1.num_tests()