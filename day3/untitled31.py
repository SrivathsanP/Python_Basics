# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 23:25:53 2022

@author: sriva
"""

items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))
