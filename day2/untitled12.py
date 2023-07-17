# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 23:43:25 2022

@author: sriva
"""

import math
r=float(input("enter radius"))
p=math.pi
s=math.pow(r, 2)
area=p*s
circ=2*p*r
print(round(area,2))
print(round(circ,2))

#round is used for rounding the digits
#round(x,y)