# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 21:13:53 2019

@author: jaredalbert
"""
import pytest

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

pytest #test_answer()


#
#def hello_name(name):
#    return(f'hello {name}')
#    
#
#
#
#def test_hello_name():
#    assert hello_name('Jared') == 'hello Jarred'

pytest
#import unittest
#class TestHello(unittest.TestCase):
#    def test_hello_name(self):
#        self.assertAlmostEqual(hello_name('bob'), 'hello bob')
#        
#if __name__ =='__main__':
#    unittest.main()