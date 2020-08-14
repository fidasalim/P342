# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 16:21:54 2020

@author: fida

Create 3x3 matrices M=(a11,a12 … a33) and N=(b11,b12, …, b33) with numbers of your
       choice (zeros, negatives and positives but not random numbers) in two separate files. Read
       the matrices from the files. Find M x A and M x N.

"""
M = []
N = []
A = []
with open('M.txt','r') as M_matrix:
    for line in M_matrix:
        sval = line.rstrip('\n').split(' ')
        sval = [float(i) for i in sval]
        M.append(sval)  
M_matrix.close()
with open('N.txt','r') as N_matrix:
    for line in N_matrix:
        sval = line.rstrip('\n').split(' ')
        sval = [float(i) for i in sval]
        N.append(sval)  
N_matrix.close()
with open('A.txt','r') as A_matrix:
    for line in A_matrix:
        sval = line.rstrip('\n').split(' ')
        sval = [float(i) for i in sval]
        A.append(sval)  
A_matrix.close()

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
The matrix M is [[1.0, 2.0, -3.0], [4.0, -5.0, 6.0], [0.0, 8.0, 9.0]]
The matrix N is [[4.0, 9.0, -7.0], [0.0, 6.0, 2.5], [9.0, -1.0, 8.0]]
The matrix A is [[2.0], [-3.5], [4.0]]
MxN = [[-23.0, 24.0, -26.0], [70.0, 0.0, 7.5], [81.0, 39.0, 92.0]]
MxA = [[-17.0], [49.5], [8.0]]
"""