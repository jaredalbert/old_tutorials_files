# -*- coding: utf-8 -*-
"""
Created on Sat May 12 11:28:38 2018

@author: jaredalbert
"""
month_days = {'palceholder': 0, 'january': 31, 'march': 30}

def day_in_month(month):
    
    return month_days[month.lower()]

print(day_in_month('JANUARY'))