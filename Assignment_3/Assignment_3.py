# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:45:23 2020

@author: fida
partial pivoting,Gauss-Jordan method,matrix multiplication

"""
n = 0
r = 0
A = []
B = []

#for partial pivoting
def par_piv(r,M = [] , N = []):
    U = []
    V = []
    n = len(M)
    for i in range(r, n):
        if M[i][i] == 0:
            for k in range(i+1, n):
                if abs(M[i][i]) < abs(M[k][i]):
                    U = M[i]
                    M[i] = M[k]
                    M[k] = U
                    V = N[i]
                    N[i] = N[k]
                    N[k] = V
                else:
                    continue
                
#for Gauss-Jordan method
def gjmeth(A = [], B = []):
    X = [x[:] for x in A]
    Y = list(B)
    n = len(X)
    for r in range(0,n):
        par_piv(r,X,Y)
        pivot = X[r][r]
        for i in range(0,n):
            X[r][i] /= pivot
        Y[r] /= pivot
        for k in range(0,n):
            if k == r or X[k][r] == 0:
                continue
            else:
                factor = X[k][r]
                for j in range(0,n):
                    X[k][j] -= factor*X[r][j]
                Y[k] -= factor*Y[r]
    return Y

#for matrix_multiplication                                
def mat_mult(X = [], Y = []):
    Z = [[0 for y in range(len(Y[0]))]for x in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(X[0])):
                Z[i][j]+=X[i][k]*Y[k][j]  
    return Z

           
"""
Q1. Solve :
	x + 3y + 2z = 2
	2x + 7y + 7z = -1
	2x + 5y + 2z = 7
"""
print('Q1 solution') 
Q1_X = []
Q1_Y = []
with open('Q_1.txt','r') as Q1_matrix:
    for line in Q1_matrix:
        sval = line.rstrip('\n').split(' ')
        sval = [float(i) for i in sval]
        cval = sval[-1]
        del sval[-1]
        Q1_X.append(sval) 
        Q1_Y.append(cval)
Q1_matrix.close()
print('X = {}\nY = {}'.format(Q1_X,Q1_Y)) 
print('The solution for the linear equation = [x,y,z] = {}\n'.format(gjmeth(Q1_X,Q1_Y)))
"""
Q2. Solve :
2y + 5z = 1
3x – y + 2z = - 2
 x – y + 3z = 3
"""
print('Q2 solution') 
Q2_X = []
Q2_Y = []
with open('Q_2.txt','r') as Q2_matrix:
    for line in Q2_matrix:
        sval = line.rstrip('\n').split(' ')
        sval = [float(i) for i in sval]
        cval = sval[-1]
        del sval[-1]
        Q2_X.append(sval) 
        Q2_Y.append(cval)
Q2_matrix.close()
print('A = {}\nB = {}'.format(Q2_X,Q2_Y)) 
print('The solution for the linear equation [x,y,z] = {}\n'.format(gjmeth(Q2_X,Q2_Y)))
"""
Q3.Find the inverse of the matrix (FYI inverse exists) and check A A-1 = I :
        1   -3    7
  A =  -1    4   -7
       -1    3   -6
""" 
print('Q3 solution')      
Q3_X = []
with open('Q_3.txt','r') as Q3_matrix:
    for line in Q3_matrix:
        sval = line.rstrip('\n').split(' ')
        sval = [float(i) for i in sval]
        Q3_X.append(sval) 
Q3_matrix.close()
print('A = {}'.format(Q3_X)) 
Q3_Y = [[0 for y in range(len(Q3_X))]for x in range(len(Q3_X))]
B = [0.0 for j in range(len(Q3_X))]
for i in range(len(Q3_X)):
    B[i] = 1.0
    for k in range(len(B)):
        Q3_Y[k][i] = gjmeth(Q3_X,B)[k]
    B = [0 for l in range(len(Q3_X))]
print('A^-1 = {}'.format(Q3_Y))  
#checking A*A^-1 = I
print('A*A^-1 = {}*{} \n= {}'.format(Q3_X,Q3_Y,mat_mult(Q3_X,Q3_Y)))
#checking A^-1*A = I
print('A^-1*A = {}*{} \n= {}'.format(Q3_Y,Q3_X,mat_mult(Q3_Y,Q3_X)))
"""
    
Q1 solution
X = [[1.0, 3.0, 2.0], [2.0, 7.0, 7.0], [2.0, 5.0, 2.0]]
Y = [2.0, -1.0, 7.0]
The solution for the linear equation = [x,y,z] = [3.0, 1.0, -2.0]

Q2 solution
A = [[0.0, 2.0, 5.0], [3.0, -1.0, 2.0], [1.0, -1.0, 3.0]]
B = [1.0, -2.0, 3.0]
The solution for the linear equation [x,y,z] = [-2.0, -2.0, 1.0]

Q3 solution
A = [[1.0, -3.0, 7.0], [-1.0, 4.0, -7.0], [-1.0, 3.0, -6.0]]
A^-1 = [[-3.0, 3.0, -7.0], [1.0, 1.0, 0.0], [1.0, 0.0, 1.0]]
A*A^-1 = [[1.0, -3.0, 7.0], [-1.0, 4.0, -7.0], [-1.0, 3.0, -6.0]]*[[-3.0, 3.0, -7.0], [1.0, 1.0, 0.0], [1.0, 0.0, 1.0]] 
= [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
A^-1*A = [[-3.0, 3.0, -7.0], [1.0, 1.0, 0.0], [1.0, 0.0, 1.0]]*[[1.0, -3.0, 7.0], [-1.0, 4.0, -7.0], [-1.0, 3.0, -6.0]] 
= [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
"""
