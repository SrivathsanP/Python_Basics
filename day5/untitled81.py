# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 00:41:17 2022

@author: sriva
"""

# importing Numpy package
import numpy as np

# creating a 2X2 Numpy matrix
arr = np.array([[50, 29,1], [30, 44,1],[1,1,1]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(arr)

# calculating the determinant of matrix
det = np.linalg.det(arr)

print("\nDeterminant of given 3x3 matrix:")
print(int(det))
