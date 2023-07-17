# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:10:02 2022

@author: sriva
"""

#pie2h
#2pierh+ 2pier2
import math as i
r=int(input('radius:'))
h=int(input('height:'))

a=i.pi
sa=(2*a*r*h)+((2*a)*i.pow(r,2))
vol=(i.pow(a,2)*r*h)
print('surface area:',sa)
print('volume:',vol)
