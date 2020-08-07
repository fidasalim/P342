# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:18:53 2020

@author: fida
"""
"""
3) sum over 1+1/2 + 1/3 + ... till the sum does not change by more than 0.001

"""
total = 1
n=1
term = 1
while term > 0.001:
    term = 1/(n+1)
    total = total + 1/(n+1)
    n=n+1
print ("The sum of",n, "term is",total)
