# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 10:39:40 2022

@author: sriva
"""

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))