# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:56:22 2022

@author: sriva
"""

import textwrap
sample=input("enter: ")
woi=textwrap.dedent(sample)
wrapped=textwrap.fill(sample,width=50)
final=textwrap.indent(wrapped, '>')
print()
print(final)
print()
