# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 19:22:13 2019

@author: jaredalbert
"""

a="75, 95 64, 17 47 82, 18 35 87 10, 20 04 82 47 65, 19 01 23 75 03 34, 88 02 77 73 07 63 67, 99 65 04 28 06 16 70 92, 41 41 26 56 83 40 80 70 33, 41 48 72 33 47 32 37 16 94 29, 53 71 44 65 25 43 91 52 97 51 14, 70 11 33 28 77 73 17 78 39 68 17 57, 91 71 52 38 17 14 91 43 58 50 27 29 48, 63 66 04 68 89 53 67 30 73 16 69 87 40 31, 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
b=a.split(", ")
d=[]
ans=0
for x in range(len(b)):
    b[x]= b[x].split(" ")
    c= [int(i) for i in b[x]]
    d.append(c)
    print(d)
#index= d[0].index(max(d[0]))
print (type(d))
#for y in range(len(d)):
#    ans+= d[y][index]
#    if y+1==len(d):
#        break
#    else:
#        index= d[y+1].index(max(d[y+1][index], d[y+1][index+1]))
#print (ans)