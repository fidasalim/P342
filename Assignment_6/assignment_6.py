# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:00:18 2020

@author: fida
"""


import assignment_6_library as lib
print('Question_2')
#Question_2
a = 1
b = 3
f2 = lib.f2
A = []
N = []
Z = []
#1.30685
#Midpoint_method
for j in (lib.Midpoint_method,lib.Trapezoidal_method,lib.Simpson_method):
    if j == lib.Simpson_method:
        for i in (6,10,26):
            print('The {}_integration of {} from {} to {} for N = {} is {} '.format(j.name,f2.name,a,b,i,j(f2,a, b, i)))  
    else:
        for i in (5,10,25):
            print('The {}_integration of {} from {} to {} for N = {} is {}.'.format(j.name,f2.name,a,b,i,j(f2,a, b, i)))
    print('\n')
 
print('Question_3')
#Question_3
a = 0
b = 1
f3 = lib.f3
for j in (lib.Midpoint_method,lib.Trapezoidal_method,lib.Simpson_method):
    N = lib.N_value(f3, a, b, 0.001,j.name)
    print('The N in {}_integration for min error to be 0.001 is {}.'.format(j.name,N))
    print('The {}_integration of {} from {} to {} is {}.\n'.format(j.name,f3.name,a,b,j(f3,a, b, N)))

#Question_4
a = 0
b = 1
f4 = lib.f4
lib.Monte_carlo(f4,a,b,10)

"""
Question_2
The Midpoint_integration of x/(1+x) from 1 to 3 for N = 5 is 1.308092114284065.
The Midpoint_integration of x/(1+x) from 1 to 3 for N = 10 is 1.3071646395900398.
The Midpoint_integration of x/(1+x) from 1 to 3 for N = 25 is 1.3069028019555275.


The Trepizoidal_integration of x/(1+x) from 1 to 3 for N = 5 is 1.3043650793650796.
The Trepizoidal_integration of x/(1+x) from 1 to 3 for N = 10 is 1.3062285968245722.
The Trepizoidal_integration of x/(1+x) from 1 to 3 for N = 25 is 1.306752839424082.


The Simpson_method_integration of x/(1+x) from 1 to 3 for N = 4 is 1.3067460317460315 
The Simpson_method_integration of x/(1+x) from 1 to 3 for N = 10 is 1.3068497693110694 
The Simpson_method_integration of x/(1+x) from 1 to 3 for N = 26 is 1.3068527513069685 


Question_3
The N in Midpoint_integration for min error to be 0.001 is 10.
The Midpoint_integration of exp(-x^2) from 0 to 1 is 0.7471308777479975.

The N in Trepizoidal_integration for min error to be 0.001 is 13.
The Trepizoidal_integration of exp(-x^2) from 0 to 1 is 0.7464612610366895.

The N in Simpson_method_integration for min error to be 0.001 is 4.
The Simpson_method_integration of exp(-x^2) from 0 to 1 is 0.7468553797909872.
"""