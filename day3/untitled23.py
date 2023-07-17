# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 11:07:49 2022

@author: sriva
"""

def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]
	  
print(change_sring('abcd'))
print(change_sring('12345'))
