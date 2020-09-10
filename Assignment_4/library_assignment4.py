# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 10:53:40 2020

@author: fida
"""

#for reading and writing the matrix from txt files
def read_matrix(x):
    X = []
    with open(x,'r') as matrix:
        for line in matrix:
            sval = line.rstrip('\n').split(' ')
            sval = [float(i) for i in sval]
            X.append(sval) 
    return(X)

#for seperating the matrix into Ax
def seperate_matrix(X = []):
    A = []
    B = []
    C = [x[:] for x in X]
    for sval in C:
        cval = sval[-1]
        del sval[-1]
        A.append(sval) 
        B.append(cval)
    return(A,B)

#for matrix_multiplication                                
def matrix_multiplication(X = [], Y = []):
    Z = [[0 for y in range(len(Y[0]))]for x in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(X[0])):
                Z[i][j]+=X[i][k]*Y[k][j]  
            if Z[i][j]<10e-12:
                Z[i][j] = 0
    return Z

#for partial pivoting
def partial_pivoting(r,M = [] , N = []):
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
                
#for LU decomposition    
def LU_decomposition(A = [] , B = []):
    X = [x[:] for x in A]
    Y = [y for y in B]
    n = len(A)
    for j in range(n):
        partial_pivoting(j,X,Y)
        for i in range(n):
            sum = 0.0
            for k in range(0,min(i,j)):
                sum += X[i][k]*X[k][j]
            if (i>j):
                X[i][j] = (X[i][j] - sum)/X[j][j]
            elif(i<j):
                X[i][j] = X[i][j] - sum
            else:
                X[i][j] = X[i][j] - sum
    return(X,Y)

#combined substitution
def substitution(A = [], B = []):
    M = [m[:] for m in A]
    N = [n for n in B]  
    n = len(M)
    Y = [0.0 for k in range(n)]
    X = [0.0 for k in range(n)]
    for i in range(n):
        sum = 0.0
        for j in range(0,i):
            sum += M[i][j]*Y[j]
        Y[i] = (N[i]-sum) 
    X = [0.0 for k in range(n)]
    #backward_substitution
    for i in range(n-1,-1,-1):
        sum = 0
        for j in range(i,n):
            sum += M[i][j]*X[j]
        X[i] = (Y[i] - sum)*1/M[i][i]
    return(X) 



#finding determinant of a tringular_matrix
def triangularmatrix_determinant(X = []):
    n = len(X)
    determinant = 1
    for i in range(n):
        determinant *= X[i][i]
    return determinant

