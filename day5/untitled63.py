# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 20:26:38 2022

@author: sriva
"""

#n=(p/100)*N
import numpy as np
   
# 1D array
arr = [20,2,7,1,34]
a=np.sort(arr)
print(a)
print("a : ", a)
print("50th percentile of a : ",
       np.percentile(a, 50))
print("25th percentile of a : ",
       np.percentile(a, 25))
print("75th percentile of a : ",
       np.percentile(a, 75))