# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:33:30 2022

@author: sriva
"""


ent=input("enter")
a=ent.split()
d=dict()
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
    