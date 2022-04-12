# -*- coding: utf-8 -*-
"""
Created on Sat May 12 08:46:21 2018

@author: jaredalbert
"""

class Employee:
    num_of_emps= 0
    raise_amount = 1.04
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
       
        
        Employee.num_of_emps += 1
    @property
    def fullname(self):
        return('{} {}'.format(self.first, self.last))
        
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
   
    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None



    @property
    def email(self):
        return self.first + '.' + self.last + '@email.com'
    
    
    
    
emp_1 = Employee('John', 'Smith')
emp_1.first = 'Nona'
emp_1.fullname = 'me too'




print (emp_1.first)
print (emp_1.email)  
print (emp_1.fullname)   

del emp_1.fullname