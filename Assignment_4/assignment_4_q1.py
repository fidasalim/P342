# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:28:16 2020

@author: fida
"""
#Q1_solution
print('Solution_Q1')

#importing the libraries
import library_assignment4 as lib

#reading the matrix 
Q1_M = lib.read_matrix('q1.txt')
#seperating matrix to square matrix and a column matrix
Q1_A , Q1_B = lib.seperate_matrix(Q1_M)

#LU_decomposition
Q1_P,Q1_Q = lib.LU_decomposition(Q1_A,Q1_B)
print('Compined LU matrix is A = {}'.format(Q1_P))

#forward and backward substitution(combined)
Q1_X = lib.substitution(Q1_P,Q1_Q)
print('Solution for AX = B, {}[x1,x2,x3,x4] = {} is\n[x1,x2,x3,x4] = {}\n'.format(Q1_A,Q1_B,Q1_X))

"""
"""
#Q2_solution
print('Solution_Q2')

#reading the matrix 
Q2_A = lib.read_matrix('q2.txt')
Q2_B = [i for i in range(len(Q2_A))]
print('The matrix A = {}'.format(Q2_A))

#LU_decomposition
Q2_P,Q2_Q = lib.LU_decomposition(Q2_A,Q2_B)

#finding determinant of the triangular_matrix
det_Q2_A = lib.triangularmatrix_determinant(Q2_P)
print('Deteminant of A =', format(det_Q2_A))
print('The determinant of A is not equal to zero,thus det(A) exists\n')

#finding inverse
Q2_Y = [[0 for y in range(len(Q2_A))]for x in range(len(Q2_A))]
I = [0.0 for j in range(len(Q2_A))]
for i in range(len(Q2_A)):
    n = Q2_Q[i]
    I[i] = 1.0
    for k in range(len(I)):
        Q2_Y[k][n] = round(lib.substitution(Q2_P,I)[k],3)
    I = [0 for l in range(len(Q2_A))]
    
print('The inverse of A is {}'.format(Q2_Y))
print('Then A*A^-1 = {} = I_4'.format(lib.matrix_multiplication(Q2_A,Q2_Y)))

"""
Solution_Q1
Compined LU matrix is A = [[1.0, 0.0, 1.0, 2.0], [0.0, 1.0, -2.0, 0.0], [1.0, 2.0, 2.0, -2.0], [2.0, 1.0, 1.5, -3.0]]
Solution for AX = B, [[1.0, 0.0, 1.0, 2.0], [0.0, 1.0, -2.0, 0.0], [1.0, 2.0, -1.0, 0.0], [2.0, 1.0, 3.0, -2.0]][x1,x2,x3,x4] = [6.0, -3.0, -2.0, 0.0] is
[x1,x2,x3,x4] = [1.0, -1.0, 1.0, 2.0]

Solution_Q2
The matrix A = [[0.0, 2.0, 8.0, 6.0], [0.0, 0.0, 1.0, 2.0], [0.0, 1.0, 0.0, 1.0], [3.0, 7.0, 1.0, 0.0]]
Deteminant of A = 36.0
The determinant of A is not equal to zero,thus det(A) exists

The inverse of A is [[-0.25, 1.667, -1.833, 0.333], [0.083, -0.667, 0.833, 0.0], [0.167, -0.333, -0.333, 0.0], [-0.083, 0.667, 0.167, 0.0]]
Then A*A^-1 = [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [-0.0, -0.0, -0.0, 1.0]] = I_4
"""