# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:10:25 2020

@author: fida
"""
"""
2) factorial n! say for n=10 or 15, check and trap negative integers, say for -5!

"""
print("The factorial of integer \'n\' can be found")
factorial = 1
n = int(input("What is the \'n\' value ? "))
if n>0:
    for i in range(1,n+1):
        factorial *=i
    print (factorial)
else:
    print (factorial)