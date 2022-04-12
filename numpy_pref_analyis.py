# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:26:34 2018

@author: jaredalbert
"""
import numpy as np

data = np.recfromcsv('Preferreds.csv', delimiter = ',')
print(type(data))