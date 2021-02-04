# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:12:39 2021

@author: fida
"""


import Library as lib

g = -9.8

# defining functions
f4a = lambda z,y,t : g
f4b = lambda z,t : z

x_0 = 0
x_n = 5
y_0 = 2
y_n = 45
h = 0.1

#lower guess
g_1 = -10
#higher guess
g_2 = 50

print('Smaller guess of slope at t = 0  = {}'.format(g_1))
print('Larger guess slope at t = 0 = {}'.format(g_2))
T, Y, v = lib.shooting_method(f4a,f4b,h,x_0,x_n,y_0,y_n,g_1,g_2)
print('The Launch velocity v(0) = {} m/s'.format(v))

"""
Solution

Smaller guess of slope at (t=0),g_1 = -10
Larger guess slope at (t=0),g_2 = 50
The Launch velocity v(0) = 33.09999999999996 m/s
"""