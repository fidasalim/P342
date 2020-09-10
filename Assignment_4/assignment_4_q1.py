# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:28:16 2020

@author: fida
"""
#Q1_solution

#importing the libraries
import library_assignment4 as lib

#reading the matrix 
Q1_M = lib.read_matrix('q1.txt')
#seperating matrix to square matrix and a column matrix
Q1_A , Q1_B = lib.seperate_matrix(Q1_M)

#LU_decomposition
Q1_P,Q1_Q = lib.LU_decomposition(Q1_A,Q1_B)
print(Q1_P)
#forward and backward substitution(combined)
Q1_X = lib.substitution(Q1_P,Q1_Q)

print('Solution_Q1')
print('Solution for AX = B, {}[x1,x2,x3,x4] = {} is\n[x1,x2,x3,x4] = {}\n'.format(Q1_A,Q1_B,Q1_X))


#Q2_solution
#reading the matrix 
Q2_A = lib.read_matrix('q2.txt')
Q2_B = [i for i in range(len(Q2_A))]

#LU_decomposition
Q2_P,Q2_Q = lib.LU_decomposition(Q2_A,Q2_B)

#finding determinant of the triangular_matrix
det_Q2_A = lib.triangularmatrix_determinant(Q2_P)
print('Solution_Q2')
print('The matrix A = {}'.format(Q2_A))
print('Deteminant of A =', format(det_Q2_A))
print('The determinant of A is not equal to zero,thus det(A) exists\n')

#finding inverse
Q2_Y = [[0 for y in range(len(Q2_A))]for x in range(len(Q2_A))]
I = [0.0 for j in range(len(Q2_A))]
for i in range(len(Q2_A)):
    I[i-3] = 1.0
    for k in range(len(I)):
        Q2_Y[k][i] = lib.substitution(Q2_P,I)[k]
    I = [0 for l in range(len(Q2_A))]
    
print('The inverse of A is {}'.format(Q2_Y))
print('The A*A^-1 = {} = I_4'.format(lib.matrix_multiplication(Q2_A,Q2_Y)))

"""
Solution
Solution_Q1
Solution for AX = B, [[1.0, 0.0, 1.0, 2.0], [0.0, 1.0, -2.0, 0.0], [1.0, 2.0, -1.0, 0.0], [2.0, 1.0, 3.0, -2.0]][x1,x2,x3,x4] = [6.0, -3.0, -2.0, 0.0] is
[x1,x2,x3,x4] = [1.0, -1.0, 1.0, 2.0]

Solution_Q2
The matrix A = [[0.0, 2.0, 8.0, 6.0], [0.0, 0.0, 1.0, 2.0], [0.0, 1.0, 0.0, 1.0], [3.0, 7.0, 1.0, 0.0]]
Deteminant of A = 36.0
The determinant of A is not equal to zero,thus det(A) exists

The inverse of A is [[-0.25000000000000006, 1.6666666666666672, -1.8333333333333333, 0.3333333333333333], [0.08333333333333337, -0.666666666666667, 0.8333333333333333, 0.0], [0.16666666666666666, -0.33333333333333326, -0.3333333333333333, 0.0], [-0.08333333333333333, 0.6666666666666666, 0.16666666666666666, 0.0]]
The A*A^-1 = [[1.0, 0, 0, 0], [0, 1.0, 0, 0], [0, 0, 0.9999999999999999, 0], [0, 0, 0, 1.0]] = I_4
"""