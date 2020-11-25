# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:41:10 2020

@author: fida
"""


import Assignment_7_library as lib
e = 2.71828
f1_1 = lib.f1a
f1_2 = lib.f1b
f2 = lib.f2
f3 = lib.f3
Euler_method = lib.Euler_method
Shooting_method = lib.shooting_method
RK_4 = lib.Runge_Kutta4_method_2_O
Euler_method(f1_1,100,2,e,0.1)
Euler_method(f1_2,100,3,1,0.1)
RK_4(f2,100,0,5,2,1)
Shooting_method(f3, 100, 0, 1, 1, 2*(e-1))

"""
Solution:
Guess_1 the slope at y(0):-3
Guess_2 the slope at y(0):6
"""