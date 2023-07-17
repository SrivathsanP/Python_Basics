# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 23:38:43 2022

@author: sriva
"""

import numpy as np
arr=np.array([[1,4,3],[7,5,6]])
print(arr)
a=int(input('enter the  value'))
x=np.where(np.any(arr > a,axis=1))
print(x)

