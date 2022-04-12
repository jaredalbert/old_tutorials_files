# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 20:30:34 2018

@author: jaredalbert
"""

from datetime import date, timedelta

start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    return(str(start_100days + timedelta(days = 100)))
    pass
get_hundred_days_end_date()

def get_days_between_pb_start_first_joint_pycon():
    return((pycon_date - pybites_founded ).days )
    """Return the int number of days"""
    pass
get_hundred_days_end_date()
print(type((get_days_between_pb_start_first_joint_pycon())))