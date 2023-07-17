# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:13:11 2022

@author: sriva
"""

a=input('enter')
ct=0
for i in a[:4]:
    if (i.upper() == i):
        ct+=1
if ct>=2:
    print(a.upper())
else:
    print(a)