# -*- coding: utf-8 -*-
"""
Created on Sun May 20 12:12:12 2018

@author: jaredalbert
"""


from Cat_and_dog import Cat

    

    
cat_1 = Cat('fluffy', 'brown', 10, 6)
cat_2 = Cat('muffy', 'white', 5,2)
cat_3 = Cat('duffy', 'black', 13, 8)
cat_4 = Cat('luffy', 'orange')
Ethelinas_cat = Cat('icecream', 'white', 10, 1000)
annagayles_cat = Cat('sprinkles', 'white', 3, 1000)

for i in range (20):
    cat_i = Cat()
    print(cat_i.__repr__())
#num_cats=num_of_cats()
#print (cat_1.__init__)
print (cat_1.__repr__())
#print (cat_1.__str__())
print (cat_2.nicknamer())
print(cat_4.attitude_rater())
print('cat_4', cat_4.__repr__())
#print (cat_4.num_cats)
print(Ethelinas_cat.__repr__())
print(Ethelinas_cat.attitude_rater())

print(annagayles_cat.__repr__())
print(annagayles_cat.attitude_rater())

print (annagayles_cat.nicknamer())
print (Ethelinas_cat.nicknamer())

print(cat_4.attitude_rater())
cat_3.getNumInstances()
