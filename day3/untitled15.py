# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:30:35 2022

@author: sriva
"""

dict = {}
str1="google.com"
for n in str1:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print(dict)
print(keys)
print(dict.values())