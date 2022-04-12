# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 10:52:41 2019

@author: jaredalbert
"""

def make_html(element):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            return(f'<{element}> {func(*args, **kwargs)} </{element}>')
        return wrapper
    return real_decorator

@make_html('p')
@make_html('strong')
def get_text(text='I code with PyBites'):
    return(text)

'''Calling:'''
x = get_text()
print(x)

'''Should return

<p><strong>I code with PyBites</strong></p>:'''