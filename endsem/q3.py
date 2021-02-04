# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:24:46 2021

@author: fida
"""


import Library as lib
import math as m

f1 = lambda x : x
f2 = lambda x : m.log(x,m.e)

# reading data from esem_table.dat
A,B = lib.create_two_matrix('esem_table.dat',1)

"""
(i) w(t) = w_0 + w_ct
"""
w01,wc1 = lib.least_square_fit(A,B,f1,f1)
Sxy1 = lib.least_square_fit.Sxy
Sxx1 = lib.least_square_fit.Sxx
Syy1 = lib.least_square_fit.Syy
# pearson's r
r1 = m.sqrt(Sxy1*Sxy1/(Sxx1*Syy1))

"""
(ii) ln(w(t)) = ln(w_0) - w_ct
"""
w02,wc2 = lib.least_square_fit(A,B,f1,f2)
w02 = m.exp(w02)
wc2 = -wc2
Sxy2 = lib.least_square_fit.Sxy
Sxx2 = lib.least_square_fit.Sxx
Syy2 = lib.least_square_fit.Syy
# pearson's r
r2 = m.sqrt(Sxy2*Sxy2/(Sxx2*Syy2))

print('For w(t) = w_0 + w_ct, w_c = {}, w_0 = {}, Pearsons r = {}'.format(w01,wc1,r1))
print('For lnw(t) = ln(w_0)- w_ct, w_c = {}, w_0 = {}, Pearsons r = {}'.format(w02,wc2,r2))

"""
Solution
For w(t) = w_0 + w_ct, w_c = 2.029102564102564, w_0 = -0.4747086247086247, Pearsons r = 0.9851557666128388
For lnw(t) = ln(w_0)- w_ct, w_c = 2.204008018288255, w_0 = 0.39559617454855656, Pearsons r = 0.9991179387307727

"""

