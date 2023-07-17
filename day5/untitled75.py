# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 23:29:19 2022

@author: sriva
"""

#How to access different rows of a multidimensional NumPy array?
import numpy as np
arr_mul=np.array([[1,2,3],[3,4,5],[5,6,7]])
#to access rows
print(arr_mul[[0,2]]) #accessing first nd last row
print()
print(arr_mul[[1,2]]) #1nd and 2nd row
