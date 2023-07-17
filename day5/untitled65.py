# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 21:59:25 2022

@author: sriva
"""

import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
res=arr.sum(axis=1) #addition within list
print(res)
ress=arr.sum(axis=0) #addition of all columns 
print(ress)