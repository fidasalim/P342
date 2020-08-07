# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 15:02:41 2020

@author: fida
"""
"""
1_a) add 1+2+3+ ... 100 WITHOUT using the formula n(n+1)/2
"""
total_1 = 0
for i in range(0, 101):
    total_1 += i
print ("Sum o the first 100 natural numbers is", total_1)


"""
1_b) add 1+2+3+ ... n WITHOUT using the formula n(n+1)/2
"""
print("Sum of n first natural number can also be found")
total_2 = 0
n = int(input("What is the n value? "))
for i in range(0, n+1):
    total_2 += i
print (total_2)
