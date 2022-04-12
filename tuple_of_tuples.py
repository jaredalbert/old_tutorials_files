# -*- coding: utf-8 -*-
"""
Created on Sat May 12 08:22:53 2018

@author: jaredalbert
"""

"""This is a sample program that seperates tuples from a tuple of tuples and returns the individual value pair
as a tuple of tuples"""

def a_tuple(t_of_t):#tuple_of_tuples
    name = ()
    num = ()
    
    
    for tup_pair in t_of_t:
        name = name + (tup_pair[0],)
        if tup_pair[1] in num: 
            num = num 
        else:
            num = num + (tup_pair[1],)
    print ('name', name)
    print ('num', num)    
    print (type(name))
        
        
        
        
tup_of_song_list = (('me', 100), ('you', 200), ('them', 300), ('us', 300))
a_tuple(tup_of_song_list)
