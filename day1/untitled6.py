# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 11:39:35 2022

@author: sriva
"""

f=int(input("enter in fahrenheit"))
c=int(input("enter in celcius"))
f_c=((f-32)*5)/9
c_f=(9*c)/5 + 32
print(f_c)
print(c_f)