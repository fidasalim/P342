# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:15:29 2021

@author: fida
"""
import Library as lib
import math as m 
L = 1
g = 9.8
x_m = m.pi/4
a = m.sin(x_m/2)
x_0 = 0
x_n = m.pi/2

#define_function
f2 = lambda p: 1/(m.sqrt(1-pow(a*m.sin(p),2)))

#using simpson method 
T = 4* m.sqrt(L/g)*lib.Simpson_method(f2,x_0,x_n,10)
print('Using simpson integration technique for N = 10, T = {}'.format(T))

"""
Solution

Using simpson integration technique for N = 10, T = 2.087324735636504
"""