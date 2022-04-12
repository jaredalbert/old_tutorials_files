# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 09:26:18 2018

@author: jaredalbert
"""

my_list = [x for x in range(100)]
print("my list {}".format(my_list))
for i in my_list:
    if i%2 ==0:
        for j in range (2,i):
            if j%3 ==0:
                my_list.remove(i)
print("my list odd {}".format(my_list))  