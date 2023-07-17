# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 10:53:49 2022

@author: sriva
"""

ad=int(input('enter'))
print("align left"+"{:<10d}".format(ad))
print("align right"+"{:10d}".format(ad))
print("centre justify"+"{:^10d}".format(ad)) 