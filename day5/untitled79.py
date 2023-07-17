# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 00:11:25 2022

@author: sriva
"""

import numpy as np
ar=np.array([1,2,5,6,7])
a=np.array([0,1])
new= np.concatenate((ar,a))
print(new)