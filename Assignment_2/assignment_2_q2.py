# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:57:46 2020

@author: fida

Create two vectors of type A=(a1,a2,a3) and B=(b1,b2,b3) with numbers of your choice (but
       not random numbers) in the code itself. Find A+B and A.B (dot product). (marks 3)
    
"""
A = [[2],[3],[4]]
B = [[5],[6],[7]]
print('The matrix A is {}'.format(A))
print('The matrix B is {}'.format(B))
C = [[0 for x in range(1)] for y in range(3)] 
D = [[0 for x in range(1)] for y in range(3)] 
for i in range(3):
    C[i][0] = A[i][0]+B[i][0]
    D[i][0] = A[i][0]*B[i][0]
print ('A+B = {}'.format(C))
print ('A.B = {}'.format(D))

"""
Solution:
The matrix A is [[2], [3], [4]]
The matrix B is [[5], [6], [7]]
A+B = [[7], [9], [11]]
A.B = [[10], [18], [28]]
"""