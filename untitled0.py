# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:12:31 2019

@author: jaredalbert
"""
import numpy as np
from time import time
from functools import wraps

np.random.seed(1)

def timer_wrap(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        to_time = func(*args, **kwargs)
        end = time() 
        print (f'Function ran in: {(end - start):.{4}} seconds')        
        return (to_time)
    return(wrapper)
"""find probabilities of matching birthdays in a room of n people"""


@timer_wrap
def main():
    size = 70
    count = 0
    total = 1000
    for n in range(total):
        match = np.random.choice(365, size, replace = True)
        if len(set(match)) != 50:
            count += 1
    return (count/total)

if __name__ == '__main__':
    print(main())
