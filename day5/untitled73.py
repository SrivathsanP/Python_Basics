# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 22:57:27 2022

@author: sriva
"""

import numpy as np
ar=np.array([1,2,0,4,0])
for i in ar:
    if ar[i]==0:
        print('index:',i)
