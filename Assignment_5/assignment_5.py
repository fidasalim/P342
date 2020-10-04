# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:27:43 2020

@author: fida
"""

import library_assignment_5 as lib
f1 = lib.f1
f2 = lib.f2
P = [1,-3,-7,27,-18]
R = []
print('***\nQuestion_1(a)\n')
print('(i) Using bisection method,\n the solution x for f1(x) = {} = 0 is ({})\n'.format(f1.name,lib.bisection_method(f1,1.5,2.5)))
print('(ii) Using regular_falsi method,\n the solution x for f1(x) = {} = 0 is {}\n'.format(f1.name,lib.regula_falsi(f1,1.5,2.5)))
print('(iii) Using newton_rapsi method,\n the solution x for f1(x) = {} = 0 is {}\n'.format(f1.name,lib.newton_raphson(f1, 1.5)))
print('***\nQuestion_1(b)\n')
print('(i) Using bisection method,\n the solution x for f2(x)= {} = 0 is  ({})\n'.format(f2.name,lib.bisection_method(f2,3,5)))
print('(ii) Using regular_falsi method,\n the solution x for f2(x) = {} = 0 is {}\n'.format(f2.name,lib.regula_falsi(f2,-4,0)))
print('(iii) Using newton_rapsi method,\n the solution x for f2(x) = {} = 0 is {}\n'.format(f2.name,lib.newton_raphson(f2, 2)))

#Question3
polynomial = 'x^4 -3x^3 - 7x^2 +27x^1 -18'
print('***\nQuestion_2\nThe roots of the polynomial {} is {}\n***\n'.format(polynomial,lib.polynomial_roots(7.5,P,R)))

"""
Solution:
***
Question_1(a)

(i) Using bisection method,
 the solution x for f1(x) = logx-sinx = 0 is ((2.219085693359375, '+-', 3.0517578125e-05))

(ii) Using regular_falsi method,
 the solution x for f1(x) = logx-sinx = 0 is (2.2191071418525734, '+-', 9.671651568510242e-08)

(iii) Using newton_rapsi method,
 the solution x for f1(x) = logx-sinx = 0 is (2.2191071489137406, '+-', 0.0)

***
Question_1(b)

(i) Using bisection method,
 the solution x for f2(x)= -x-cosx = 0 is  ((-0.7390689849853516, '+-', 4.76837158203125e-05))

(ii) Using regular_falsi method,
 the solution x for f2(x) = -x-cosx = 0 is (-0.7390851331687155, '+-', 4.101931860844843e-08)

(iii) Using newton_rapsi method,
 the solution x for f2(x) = -x-cosx = 0 is (-0.7390851332151608, '+-', 0.0)

***
Question_2
The roots of the polynomial x^4 -3x^3 - 7x^2 +27x^1 -18 is [3.000000000033364, 1.9999999999218425, 1.0000000000476508, -3.0000000000028573]
***
"""
