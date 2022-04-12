# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 09:07:49 2018

@author: jaredalbert
"""
from sqlalchemy import create_engine, MetaData, Table
engine = create_engine('postgresql://postgres:ja7359##@localhost:5432/sample_db')
                       
connection = engine.connect()

employee = Table('employee2', metadata, autoload = True, autoload_with = engine)
print(repr(census))

