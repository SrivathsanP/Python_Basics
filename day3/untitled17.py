# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 10:46:56 2022

@author: sriva
"""

str1='restart'
char=str1[0]
str1=str1.replace(char,'$')
print(str1)
str1 = char + str1[1:]
print(char)
print(str1)
