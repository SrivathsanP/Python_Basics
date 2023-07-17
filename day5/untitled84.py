# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 00:54:48 2022

@author: sriva
"""


#(a+ib) \times (x+iy)=ax+i^2by+i(bx+ay)=ax-by+i(bx+ay)
# importing numpy as library
import numpy as np


# creating matrix of complex number
x = np.array([2+3j, 4+5j])
print("Printing First matrix:")
print(x)

y = np.array([8+7j, 5+6j])
print("Printing Second matrix:")
print(y)

# vector dot product of two matrices
z = np.vdot(x, y)
print("Product of first and second matrices are:")
print(z)
