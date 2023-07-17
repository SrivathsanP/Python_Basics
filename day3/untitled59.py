# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 13:33:46 2022

@author: sriva
"""

x = 3
y = 123
print("\nOriginal Number: ", x)
print("Formatted Number(left padding, width 2): "+"{:0>2d}".format(x));
print("Original Number: ", y)
print("Formatted Number(left padding, width 5): "+"{:0>5d}".format(y));
