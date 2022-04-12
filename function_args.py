# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 14:12:05 2022

@author: Windows10
"""
shopping_list = {}

def show_list(shopping_list, include_quantities=True):
    print()
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f'{quantity}x {item_name}')
        else:
            print(item_name)
            
def add_items(shopping_list, **item_names):
    for item_name, quantity in item_names.items():
        shopping_list[item_name]=quantity
    
    return shopping_list

new_list = add_items(shopping_list,f=1,d=2,s=3)    

items_list = ['corn', 'bread', 'flour']

shopping_list1 = add_items(shopping_list, **new_list)

print(show_list(shopping_list1))


x=(1,2,3)
y=('a','b','c')

