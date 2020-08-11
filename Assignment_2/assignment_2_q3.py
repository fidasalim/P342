# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:21:54 2020

@author: fida

Create 3x3 matrices M=(a11,a12 … a33) and N=(b11,b12, …, b33) with numbers of your
       choice (zeros, negatives and positives but not random numbers) in two separate files. Read
       the matrices from the files. Find M x A and M x N.

"""
from matrix_AB import A
from matrix_M import M
from matrix_N import N

print('The matrix M is {}'.format(M))
print('The matrix N is {}'.format(N))
print('The matrix A is {}'.format(A))
"""
MxN
"""
O = [[0 for y in range(len(N))]for x in range(len(M[0]))]
for i in range(len(M[0])):
    for j in range(len(N)):
        for k in range(len(M)):
            O[i][j]+= M[i][k]*N[k][j]        
print ("MxN = {}".format(O))

"""
MxA
"""
Q = [[0 for x in range(len(A[0]))]for y in range(len(M))]
for i in range(len(M)):
    for j in range(len(A[0])):
        for k in range(len(M)):
            Q[i][j]+= M[i][k]*A[k][j]        
print ("MxA = {}".format(Q))

"""
Solution:
The matrix M is [[1, 2, -3], [4, -5, 6], [0, 8, 9]]
The matrix N is [[4, 9, -7], [0, 6, 2], [9, -1, 8]]
The matrix A is [[2], [3], [4]]
MxN = [[-23, 24, -27], [70, 0, 10], [81, 39, 88]]
MxA = [[-4], [17], [60]]
"""