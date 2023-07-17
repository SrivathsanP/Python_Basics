# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:42:09 2022

@author: sriva
"""
'''
import math as i 
bi=int(input('enter the binary number'))
an=bi
a=0
r=0
while (bi!=0):
    n=bi%10
    a=a+(i.pow(2,r))
    d=bi/10
    r+=1
print("decimal:",a)
    
'''

    
b_num = list(input("Input a binary number: "))
value = 0

for i in range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)
