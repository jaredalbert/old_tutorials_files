# -*- coding: utf-8 -*-
"""
Created on Sat May 19 13:14:38 2018

@author: jaredalbert
"""

print('Imorted my_module....')
test = 'Test String'


def find_index(to_search, target):
    '''find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1
    

test_list =[1 ,3 ,5 ,6 ,7]

#print(find_index(test_list, 7))