# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 21:47:48 2018

@author: jaredalbert
"""
import re
y = []
x = ['$1','$4','$5']
for item in x:
    y.append( re.sub('\$',' ', item))
print(y)