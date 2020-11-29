# -* coding: utf-8 -*-
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

#Question_1
Euler_method = lib.Explicit_Euler_method
H = [0.5,0.25,0.1,0.05]
#1_a
for i in range(len(H)):
    X,Y = Euler_method(H[i],f1_1,2,e,12)

#1_b
#for h = 0.5,0.25,0.1,0.05
for i in range(len(H)):
    X,Y = Euler_method(H[i],f1_2,3,1,12)


#Question_2
RK_4 = lib.Runge_Kutta4_method_2_O
H = [0.5,0.25,0.1,0.05]
for i in range(len(H)):
    X,Y = RK_4(f2,H[i],0,5,2,1)
    

#Quesion_3
Shooting_method = lib.shooting_method
H = [0.2,0.1,0.05,0.02]
for i in range(len(H)):
    print("For h = {}".format(H[i]))
    X,Y = Shooting_method(f3, H[i], 0, 1, 1, 2*(e-1))
    
"""
Solution:
Question_3
For h = 0.2

Guess_1 the slope at y(0):6
The guess a smaller slope

Guess_1 the slope at y(0):0

Guess_2 the slope at y(0):5
Using langrange extrapolation, the slope at y(0) is 1.000033596246148

For h = 0.1

Guess_1 the slope at y(0):-5

Guess_2 the slope at y(0):5
Using langrange extrapolation, the slope at y(0) is 1.0000002978151095

For h = 0.05

Guess_1 the slope at y(0):-0.8

Guess_2 the slope at y(0):2
Using langrange extrapolation, the slope at y(0) is 0.9999980298267257

For h = 0.02

Guess_1 the slope at y(0):0.5

Guess_2 the slope at y(0):3.5
Using langrange extrapolation, the slope at y(0) is 0.9999978759077419
"""