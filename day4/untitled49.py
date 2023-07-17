# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 08:48:09 2022

@author: sriva
"""
#arc=2pi r (teta/360)
import math as i
a=i.pi
dia=int(input('enter diameter'))
angle=float(input('angle:'))
if angle>=360:
    print('not possible')
    
else:
    arc=(a*dia)*(angle/360)
print('arc length :',arc)