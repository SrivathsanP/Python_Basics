# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 08:25:48 2022

@author: sriva
"""

def en(st,er):
    return st[:2] + er + st[2:]
    
print(en('[[]]','python'))
print(en('{{}}','Php'))
