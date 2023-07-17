# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 21:50:18 2022

@author: sriva
"""

import numpy as np
arr=np.array([[10,15,30,65],[80,87,100,np.nan]])
print(arr)
print('\n')
print(np.diff(arr,axis=1))