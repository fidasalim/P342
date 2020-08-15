# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:57:46 2020

@author: fida

Create two vectors of type A=(a1,a2,a3) and B=(b1,b2,b3) with numbers of your choice (but
       not random numbers) in the code itself. Find A+B and A.B (dot product). (marks 3)
    
"""
A = [2,-3.5,4]
B = [5,6,-7]
print('The vector A is {}'.format(A))
print('The vector B is {}'.format(B))
C = [0 for x in range(3)]
D = [0 for x in range(3)]
for i in range(3):
    C[i] = A[i]+B[i]
    D[i]= A[i]*B[i]
print ('A+B = {}'.format(C))
print ('A.B = {}'.format(D))

"""
Solution:
The vector A is [2, -3.5, 4]
The vector B is [5, 6, -7]
A+B = [7, 2.5, -3]
A.B = [10, -21.0, -28]
"""