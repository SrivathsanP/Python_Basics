# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 10:28:52 2022

@author: sriva
"""

int1=int(input('enter-'))
int2=int(input('enter:'))
#prefix to add 0
print("Formatted Number(left padding, width 3):"+"{:0>2d}".format(int1));
print("Formatted Number(left padding, width 6):"+"{:0>6d}".format(int2));