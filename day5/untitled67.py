# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 22:12:55 2022

@author: sriva
"""

import numpy as np
x=np.array([1,2,-4])
print(x)
neg=np.negative(x)
pos= -x
assert np.array_equal(neg,pos)
print(neg)
