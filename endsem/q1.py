# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:57:45 2021

@author: fida
"""


import Library as lib
import math as m 

#defining the function
f1 = lambda x : ((x-5)*m.exp(x)) + 5
setattr(f1,'name','(x-5)e^x + 5')

h = 6.626*1.0e-34
k = 1.381*1.0e-23
c = 3*1.0e8
# error 
err = 1.0e-4

#implimenting newton_raphson
value,error = lib.newton_raphson(f1,5,err)

#wein constant b
b = (h*c)/(k*value)

#error in b
errorb = error*b/value
print('Using Newton-Raphson, the solution for {} = 0, is {} +\- {}'.format(f1.name, value, error))
print('Wein  constant, b = {} m K +\- {} m K'.format(b,errorb))

"""
Solution

Using Newton-Raphson, the soution for (x-5)e^x + 5 = 0, is 4.965114231747178 +\- 1.4552064087069994e-06
Wein  constant, b = 0.0028990103307365983 m K +\- 8.496598900426886e-10 m K
"""

