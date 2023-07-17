# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 00:06:41 2022

@author: sriva
"""

import numpy as np
  
# using numpy.fill_diagonal() method
array = np.array([[1, 2], [2, 1]])
np.fill_diagonal(array, 0)
  
print(array)