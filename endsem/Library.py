# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:59:51 2021

@author: fida
"""
import matplotlib.pyplot as plt
import math as m
import random as random


"""
NEWTON_RAPHSON
"""
def newton_raphson(u,a,err):
    x = a
    flag = True
    i = 1
    x_values = [x]
    error = []
    e = err
    #using newton_raphson get the solution
    while(flag == True):
        du = single_derivative(u,x)
        x = x - u(x)/du
        x_values.append(x)
        error.append(abs(x - x_values[i-1]))
        if error[-1]<e:
            flag = False  
        i+=1
        #stop the loop if iteration exceeds 200
        if i >= 200:
            print('You need to change values of x_0')
            flag = None
            return(None,None)
    #function called again if we havent got the solution
    if flag == False:
        return(x,error[-1])

"""
Simpson_method
"""
def Simpson_method(u,a,b,N):
    i = 0
    S = 0
    h = (b-a)/N
    while(i<=N):
        x = a + i*h
        if(i == 0 or i==N):
            w = 1
        elif(i % 2 == 0):
            w = 2
        else:
            w = 4
        S += (h/3)*w*u(x) 
        i += 1
    return(S)  

"""
Least Square Fit
"""
def least_square_fit(X,Y,u,v):
    N = len(X)
    sum_x = 0
    sum_xx = 0
    sum_xy = 0
    sum_y = 0
    sum_yy = 0
    for i in range(0,N):
        sum_x += u(X[i])
        sum_xx += u(X[i])*u(X[i])
        sum_xy += u(X[i])*v(Y[i])
        sum_y += v(Y[i])
        sum_yy += v(Y[i])*v(Y[i])
    avg_x = sum_x/N
    avg_y = sum_y/N
    delta = (N*sum_xx)-(sum_x*sum_x)
    a = ((sum_y*sum_xx)-(sum_x*sum_xy))/delta
    b = ((N*sum_xy)-(sum_x*sum_y))/delta
    least_square_fit.Sxx = sum_xx - N*avg_x**2
    least_square_fit.Syy = sum_yy - N*avg_y**2
    least_square_fit.Sxy = sum_xy - N*avg_x*avg_y
    least_square_fit.S = m.sqrt((least_square_fit.Syy-(b*least_square_fit.Sxy))/(N-2))
    least_square_fit.delta_a = least_square_fit.S*m.sqrt((1/N)+(avg_x**2)/least_square_fit.Sxx)
    least_square_fit.delta_b = least_square_fit.S/m.sqrt(least_square_fit.Sxx)
    return(a,b)  


#create two matrix from a data file
def create_two_matrix(data,j): 
    X = []
    Y = []
    with open(data,'r') as X_matrix:
        for line in X_matrix:
            sval = line.rstrip('\n').split('\t')
            sval = [float(i) for i in sval]
            uval = sval[0]
            X.append(uval) 
            Y.append(sval[1])
    X_matrix.close()
    return(X,Y)

#Runge_Kutta4 _method_for second order DE  u function for dv/dt and v function for dx/dt
def Runge_Kutta4_method(u,v,h,x_0,x_n,y_0,z_0):
    X = [x_0]
    Y = [y_0]
    Z = [z_0]
    x = x_0
    y = y_0
    z = z_0
    N = int((x_n - x_0)/h)
    for n in range(N):
        #defining k1,k2,k3,k4 for all the y and dy/dx
        k1y = h*v(z,x)
        k1z = h*u(z,y,x)
        k2y = h*v(z + k1z/2,x+h/2)
        k2z = h*u(z+ k1z/2,y + k1y/2,x + h/2)
        k3y = h*v(z + k2z/2,x+h/2)
        k3z = h*u((z+k2z/2),(y + k2y/2),(x + h/2))
        k4y = h*v(z + k3z,x+h)
        k4z = h*u((z+k3z),(y + k3y),(x + h))
        x += h
        #new y and new dy/dx on a small increment of dx = h
        y = y + 1/6*(k1y+(2*k2y)+(2*k3y)+k4y)
        z = z + 1/6*(k1z+(2*k2z)+(2*k3z)+k4z)
        X.append(x)
        Y.append(y)
        Z.append(z)
    return(X,Y,Z)

#shooting method along with RK4, l is the slope at a 
def shooting_method(u,v,h,a,b,y_a,y_b,g_1,g_2):
        #defining slope1
        M,N1,O1 = Runge_Kutta4_method(u,v,h,a,b,y_a,g_1)
        #correcting slope 1 to ve less than 0
        while (round(N1[-1]-y_b,5) >0):
            print('The guess a smaller slope')
            return (None,None,None)
        if round(N1[-1] - y_b,5)!= 0:
            #defining slope 2 
            M,N2,O2 = Runge_Kutta4_method(u,v,h,a,b,y_a,g_2)
            #correcting slope to be greater than 0
            while (round(N2[-1]-y_b,5)<0):
                print('The guess a larger slope')
                return (None,None,None)
            #lagrange_interpolation
            if (round(N2[-1]-y_b,5) == 0):
                return(M,N2,g_2)
            l = g_1 + (g_2 - g_1)*(y_b-N1[-1])/(N2[-1]-N1[-1])
            M,N1,O2 = Runge_Kutta4_method(u,v,h,a,b,y_a,l)
            return(M,N1,l)
        else:
            return(M,N1,g_1)


"""
matrix_from_text_file
"""
def read_matrix(name):
    A = []
    with open(name,'r') as A_matrix:
        for line in A_matrix:
            sval = line.rstrip('\n').split(' ')
            sval = [float(i) for i in sval]
            A.append(sval) 
    A_matrix.close()
    return(A)

"""
matrix_multiplication
"""
def matrix_multiplication(M,N):
    O = [[0 for y in range(len(N[0]))]for x in range(len(M))]
    for i in range(len(M)):
        for j in range(len(N[0])):
            for k in range(len(M[0])):
                O[i][j]+= M[i][k]*N[k][j] 
    return(O)

"""
matrix_addition
"""
def matrix_addition(M,N):
    if len(M) == len(N) and len(M[0]) == len(N[0]):
        O = [[0 for y in range(len(N[0]))]for x in range(len(M))]
        for i in range(len(M)):
            for j in range(len(N[0])):            
                    O[i][j] =  M[i][j]+N[i][j] 
        return(O)
    else:
        print('matrix_addition_not_possible')
        return(None)

"""
Guass_jordan
"""
#partial_pivot
def partial_pivot(r,M = []):
    U = []
    m = len(M)
    for i in range(r, m):
        if M[i][i] == 0:
            for k in range(i+1, m):
                if abs(M[i][i]) < abs(M[k][i]):
                    U = M[i]
                    M[i] = M[k]
                    M[k] = U
                else:
                    continue
        else:
            continue
        
#Gauss_jordan_find the solution for linear equation
def gauss_jordan_method(X = []):
    A = [x[:] for x in X]
    B = []
    m = len(A)
    n = len(A[0])
    for r in range(0,m):
        partial_pivot(r,A)
        pivot = A[r][r]
        for i in range(0,n):
            A[r][i] /= pivot
            if pivot == 0:
                    return(None)
            else:
                for k in range(0,m):
                    if k == r or A[k][r] == 0:
                        continue
                    else:
                        factor = A[k][r]
                        for j in range(0,n):
                            A[k][j] -= factor*A[r][j]
    for k in range(0,m):
        B.append(A[k][m:n])
    return B     


#create Augmented matrix, data = '.txt', j = 1 if last element has to be emitted
def create_Aug_matrix(data,j): 
    X = []
    Y = []
    A = []
    with open(data,'r') as X_matrix:
        for line in X_matrix:
            sval = line.rstrip('\n').split('\t')
            sval = [float(i) for i in sval]
            A.append(sval)
            uval = sval[:len(sval)-j]
            X.append(uval) 
            Y.append(sval[-j:])
    X_matrix.close()
    return(X,Y,A)



#seperate data into two matrices


#find_inverse(define I in the main)
def matrix_inverse(A,I):
    B = [x[:] for x in A]
    for i in range(len(B)):
        for j in range(len(I)):
            B[i].append(I[i][j])
    I = gauss_jordan_method(B)
    return(I)


"""
LU_decomposition
"""
def partial_pivotLU(r,M = [] , N = []):
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
        else:
            continue

#for LU decomposition    
def LU_decomposition(A = [] , B = []):
    X = [x[:] for x in A]
    Y = [y[:] for y in B]
    n = len(A)
    for j in range(n):
        partial_pivotLU(j,X,Y)
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

#substitution
def substitution(A = [], B = []):
    M = [m[:] for m in A]
    N = [n[:] for n in B]
    m = len(M)
    n = len(N[0])
    Y = [[0 for y in range(n)]for x in range(m)]
    #forward
    for i in range(m):
        sum_ = 0.0
        for j in range(0,i):
            sum_ += M[i][j]*Y[j][0]
        Y[i][0] = (N[i][0]-sum_) 
    X = [[0 for y in range(n)]for x in range(m)]
    #backward_substitution
    for i in range(m-1,-1,-1):
        sum_ = 0
        for j in range(i,m):
            sum_ += M[i][j]*X[j][0]
        X[i][0] = (Y[i][0] - sum_)*1/M[i][i]
    return(X) 


#finding determinant of a tringular_matrix
def triangularmatrix_determinant(X = []):
    n = len(X)
    determinant = 1
    for i in range(n):
        determinant *= X[i][i]
    return determinant

#find inverse exist and find the inverse
def inverse_4matrix(A):
    B = [[i for x in range(1)]for i in range(len(A))]
    X,Y = LU_decomposition(A,B)
    if triangularmatrix_determinant(X) != 0:
        I = [[0.0 for y in range(len(A))]for x in range(len(A))]
        P = [[0.0 for i in range(1)]for j in range(len(A))]
        print(I)
        for i in range(len(A)):
            n = Y[i][0]
            P[i][0] = 1.0
            for k in range(len(I)):
                I[k][n] = round(substitution(X,P)[k][0],3)
            P = [[0 for i in range(1)]for j in range(len(A))]
    return(I)

"""
newton_raphson
"""
#introducing function and providing those function an attribute name
f1 = lambda x : m.log(x,m.e) - m.sin(x)
f2 = lambda x : -x - m.cos(x)
setattr(f1,'name','logx-sinx')
setattr(f2,'name','-x-cosx')
    
#single derivative function
def single_derivative(u,x):
    h = 0.001
    df1_x = (u(x+h)-u(x-h))/(2*h)
    return (df1_x)

#double derivative function
def double_derivative(u,x):
    h = 0.001
    df2_x = (u(x+2*h)+u(x-2*h)-(2*u(x)))/(4*(h*h))
    return (df2_x)

#triple derivative function
def triple_derivative(u,x):
    h = 0.001
    df3_x = (u(x+3*h)+u(x-h)-(2*(u(x+h)-u(x-h))+u(x+h)+u(x-3*h)))/m.pow(2*h,3)
    return (df3_x)

#fourth derivative function
def fourth_derivative(u,x):
    h = 0.001
    df4_x = (u(x+4*h)-(4*u(x+2*h))+(6*u(x))-(4*u(x-2*h))+u(x-4*h))/m.pow(2*h,4)
    return (df4_x)

"""
BISECTION
"""
def write_file(name,heading,title_1,title_2,X):
    f = open(name+'.txt',"w+")
    f.write(heading+'\n'+title_1+'\t\t'+title_2+'\n')
    for i in range(len(X)):
        f.write(str (i+1)+'\t\t'+str(X[i])+'\n')
    f.close()
    
#bracketing a and b
def bracketing_ab(u,p,q):
    a = p
    b = q
    beta = 1.5
    flag = True
    j = 0
    #choosing a and b such that u(a)<0 and u(b)>0
    while(flag): 
        # if u(a) and u(b) lies in the same side of zero 
        if u(a)*u(b)>0:
            if abs(u(a)) < abs(u(b)):
                a = a - (beta*(b-a))
            else:
                b = b + (beta*(b-a))
            j+=1
            #if the iteration exceeds 12
            if j >= 12:
                print('You need to change values of a and b')
        # when u(a) and u(b) lies in the different side of zero, we stop the loop
        else:
            flag = False 
    return(a,b)

#bisection_method
def bisection_method(u,p,q):     
    a,b = bracketing_ab(u,p,q)
    i = 1
    e = 1.0e-4
    flag = True
    bisection = []
    error = []
    title = '-Bisection_method'
    heading= '{}_({})'.format(title,u.name)
    #opening a file to save the error
    #using bisection to get closer to the solution
    while(flag == True):
        c = (a+b)/2
        bisection.append(c)
        if u(a)*u(c) <0:
            b = c
            if abs(b-a)<e:
                flag = False
        elif u(a)*u(c) >0:
            a = c
            if abs(b-a)<e:
                flag = False
        # if u(a) or u(b) = 0
        else:
            flag = False
        if i>0:
            error.append(abs(bisection[i]-bisection[i-1]))
        i=i+1
        #stop the loop if iteration exceeds 200
        if i >= 200:
            print("Choose another interval")
            flag = False 
    write_file('bisection1'+u.name,heading,'Iteraion','Absolute_error_in_c',error)
    return((a+b)/2,abs(a-b)/2) 

"""
REGULA_FALSI
"""       
def regula_falsi(u,p,q):
    a = p
    b = q
    flag = True
    i = 0
    falsi = [0]
    error = []
    e = 1.0e-6
    title = '-Regula_Falsi'
    heading= '{}_({})'.format(title,u.name)
    #opening a file to save the error
    #using regula_falsi get the solution
    #see if both the points are in the different side of f = 0
    if u(a)*u(b)<0:
        while(flag == True):
            m = (u(b)-u(a))/(b-a)
            c = b - (u(b)/m)
            falsi.append(c)
            error.append(abs(falsi[i+1]-falsi[i]))
            if abs(error[-1])<e:
                flag = False
            elif u(a)*u(c) <0:
                b = c
            else:
                a = c
            i+=1
            #stop the loop if iteration exceeds 200
            if i >= 200:
                print("Choose another interval")
                flag = False 
                return(None,None)
        write_file('regula_falsi'+u.name,heading,'Iteration','Absolute Error in c',error)
        return(c,error[-1])
    #if a and b the points are in the same side of f = 0, then the function is called again
    else:
        print('You need to change values of a and b')
        return(None,None)


  
"""
POLYNOMIAL ROOTS
"""
#defining the plynomial when the coeficients are provided
def polynomial(x,A = []):
    y = 0
    for i in range(0,len(A)):
        y += A[i]*pow(x,(len(A)-(i+1)))
    return y 
#laguerres_methos
def laguerres_method(r,A = [],R = []):
    x = r
    i = 0
    n = len(A)-1
    def p(x):
        return(polynomial(x,A))
    flag = True
    e = 1.0e-6
    #loop to find the roots of p(x) = 0
    while (flag == True):
        if p(x) == 0:
            R.append(x)
            flag = False
        else:
            dp1_x = single_derivative(p,x)
            dp2_x = double_derivative(p,x)
            g = dp1_x/p(x)
            h = g*g - (dp2_x/p(x))
            w = ((n-1)*(n*h-pow(g,2)))
            #iteration exceeds or giving an imaginary root
            if (w <0) or i >= 200:
                flag = None
            d1 = g + m.sqrt((n-1)*(n*h-pow(g,2)))
            d2 = g - m.sqrt((n-1)*(n*h-pow(g,2)))
            if abs(d1)>=abs(d2):
                a = n/d1
            else:
                a = n/d2
            x = x-a
            i+=1 
            if abs(a)<e :
                R.append(x)
                flag = False
            else:            
                continue
    #calling the function again if something went wrong
    
        
#synthetic division
def synthetic_division_method(A = [], R = []):
    B = [A[0]]
    for i in range(1,len(A)):
        b = A[i]+(R[-1]*B[i-1])
        B.append(b)
    #removing the reminder
    B.pop()
    return(B)

#function to return the roots of the polynomial
def polynomial_roots(r,P=[],R=[]):
    m = r
    S= [s for s in P]
    for i in range(0,len(P)-1):
        laguerres_method(m,S,R)
        if R == []:
            print("Choose another x_0")
        else:
            S = synthetic_division_method(S,R) 
    return(R)


"""
"""""""""""""""""""""""""""""""""""""
Intgration method
"""""""""""""""""""""""""""""""""""""
"""
f2 = lambda x : x/(1+x)
f3 = lambda x : m.exp(-m.pow(x,2))
f4 = lambda x : 4/(1+(x*x))
setattr(f2,'name','x/(1+x)')
setattr(f3,'name','exp(-x^2)')
setattr(f4,'name','4/(1+x^2)')
"""
Midpoint_method
"""
def Midpoint_method(u,a,b,N):
    M = 0
    h = float(b-a)/N
    i = 1
    while(i<=N):
        x = ((a+(i-1)*h)+(a+i*h))/2
        M += h*u(x) 
        i += 1
    return(M)

"""
Trapezoidal_method
"""   
def Trapezoidal_method(u,a,b,N):
    i = 0
    T = 0
    h = (b-a)/N
    while(i<=N):
        x = a + i*h
        if i == 0 or i == N:
            w = 1
        else:
            w = 2
        T += (h/2)*w*u(x) 
        i += 1
    return(T)
"""
"""
setattr(Midpoint_method,'name','Midpoint')
setattr(Trapezoidal_method,'name','Trepizoidal')
setattr(Simpson_method,'name','Simpson_method')
"""
"""

"""
Finding_N_value
"""
def N_value(u,a,b,error,name):
    d2f_max = max(abs(double_derivative(u,a)),abs(double_derivative(u,b)))   
    d4f_max = max(abs(fourth_derivative(u,a)),abs(fourth_derivative(u,b))) 
    if name == 'Midpoint' or name == 'Trepizoidal' or name == 'Simpson_method':
        if name == 'Midpoint':
            N = m.ceil(m.sqrt(m.pow(b-a,3)*d2f_max/(24*error)))
        if name == 'Trepizoidal':
            N = m.ceil(m.sqrt(m.pow(b-a,3)*d2f_max/(12*error)))
        if name == 'Simpson_method':
            N = m.ceil(m.pow(m.pow(b-a,5)*d4f_max/(180*error),1/4))
            if N%2==1: 
                N = N+1
    else:
        N = 0
    return N

"""
Monte_Carlo
"""
def Monte_carlo(u,N,a,b):
    j = 1
    Monte_Carlo = []
    STD = []
    for k in N:
        i = 1
        suM = 0 
        suM2 = 0
        while(i<=k):
            x = random.uniform(a,b)  
            suM += u(x)
            suM2 += u(x)*u(x)
            i+=1
        sigma = m.sqrt((suM2/k)-m.pow(suM/k,2))
        STD.append(m.sqrt(sigma))
        M_C = ((b-a)/k)*suM
        Monte_Carlo.append(M_C)
        j += 1
    return(Monte_Carlo,STD,)

"""
Data_analysis
"""
#plt.annotate("begin",(0,0))

def tabular_data(p,x,X=[],Y=[],Z=[]):
    f = open(x+'.txt',"w+")
    if p =='p':
        for i in range(len(Y)):
            f.write(str (X[i])+'\t\t'+str(Y[i])+'\t\t'+str(Z[i])+'\n')
            print(str (X[i])+'\t\t'+str(Y[i])+'\t\t'+str(Z[i])+'\n')
    else:
         for i in range(len(Y)):
            f.write(str (X[i])+'\t\t'+str(Y[i])+'\t\t'+str(Z[i])+'\n')
    f.close()

    
# plot a single graph
def plot_graph(X,Y,x,y,title,name,n,yes):
    plt.title(title) 
    plt.plot(X,Y,marker = 'o')
    if isinstance(n, float) == True:
        plt.axhline(y=n,linewidth=2, color='r')
        plt.annotate(round(n,6),(0,n))
    if yes == 'yes':
        for ij in zip(X,Y):
            plt.annotate('(%f, %f)' % ij, xy=ij, textcoords='data')
    plt.xlabel(str(x)+'---->')
    plt.ylabel(str(y)+'---->')
    plt.savefig(name+'.pdf')
    plt.show()
    
def plot_graph1(x,y,z,u,A = [],B = []):
    plt.plot(A,B,color = 'blue',marker = 'o',markerfacecolor = 'red')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(z) 
    plt.axhline(color = 'black',y = 3.14158)
    plt.savefig(u+'.pdf', dpi = 300)
    plt.show()

#plot_several data in single graph 
def plot_graph_wos(X,Y,x,y,title,label,j):
    plt.title(title)
    plt.scatter(X, Y,label = label+str(j)) 
    plt.xlabel(str(x)+'---->')
    plt.ylabel(str(y)+'---->')


def plot_curve(u,a,b,label,N):
    X,Y = analytic_function(u,a,b,N)
    plt.plot(X,Y,label = label)

import numpy as np
def analytic_function(u,x_0,x_n,N):
    x = np.linspace(x_0,x_n,N)
    y = u(x)
    return(x,y)

def plot_limit(t,x1,x2,y1,y2):
    if t == 'limx':
        plt.xlim(x1,x2)
    if t == 'limy':
        plt.ylim(y1,y2)
    if t == 'limxy':
        plt.xlim(x1,x2)
        plt.ylim(y1,y2)
    else:
        None
       
"""
"""""""
ODE
"""""""
"""
#f1a = lambda y,x : y*m.log(y)/x
b = lambda x : np.exp(x/2)

#explicit_euler_method
def Explicit_Euler_method(h,u,x_0,y_0,x_n):
    X = [x_0]
    Y = [y_0]
    N = int((x_n - x_0)/h)
    for n in range(N):
        x = X[-1]+h 
        y = Y[-1]+h*u(Y[-1],X[-1])
        X.append(x)
        Y.append(y)
    return(X,Y)

#predictor_corrector
def predictor_corrector(u,N,x_0,y_0,h):
    X = [x_0]
    Y = [y_0]
    for n in range(N):
        k1 = h*u(Y[-1],X[-1])
        y_p = Y[-1]+k1
        x = X[-1]+h
        k2 = h*u(y_p,x)
        y_c = Y[-1] + (k1+k2)/2
        X.append(x)
        Y.append(y_c)
    return(X,Y)

#Runge_Kutta_for 1 variable
def Runge_Kutta4_method_1_O(u,h,x_0,y_0,x_n):
    X = [x_0]
    Y = [y_0]
    N = int((x_n-x_0)/h)
    for n in range(N):
        k1 = h*u(Y[-1],X[-1])
        k2 = h*u((Y[-1]+k1/2),(X[-1]+h/2))
        k3 = h*u((Y[-1]+k2/2),(X[-1]+h/2))
        k4 = h*u((Y[-1]+k3),(X[-1]+h))
        x = X[-1] + h
        y = Y[-1] + 1/6*(k1+(2*k2)+(2*k3)+k4)
        X.append(x)
        Y.append(y)
    return(X,Y)



"""
project
"""
#random_walk
def plot_graph_rw(X,Y,N,j):
    plt.scatter(0,0,c='brown')
    plt.annotate("begin",(0,0))
    plt.title("Random Walk for N = {}".format(N))
    plt.plot(X, Y,label = 'r_w'+str(j+1)) 
    plt.scatter(X[-1],Y[-1], marker = 'o' ,c='black')
    plt.xlabel('x -->')
    plt.ylabel('y -->')
    plt.annotate("end",(X[-1],Y[-1]))
    
def random_walk(N,k,n,yes):
    R = R_2 = X_d = Y_d = 0.0
    #k random walk 
    for j in range(0,k):
        x = 0.;y = 0.;
        X =[x];Y=[y];
        # taking N steps for a single random walk
        for i in range(0,N):
            theta = 2*m.pi*random.random()
            x+= m.cos(theta)
            X.append(x)
            y+= m.sin(theta)
            Y.append(y)
        #R for eachrandom walk
        R += (m.sqrt(x*x + y*y))
        #R^2 for each random walk
        R_2 += (x*x + y*y)
        #X_displacement for each randomwalk
        X_d += x
        #Y_displacement for each randomwalk
        Y_d += y
        if yes == 'yes':
            if(j<n):
                plot_graph_rw(X,Y,N,j)  
    if yes == 'yes':
        plt.legend()
        plt.savefig('r_w_N={}.pdf'.format(N))
        plt.show()
    return(X,Y,R,R_2,X_d,Y_d)

#MOnte_carlo  
def Monte_carlo_Volume(u,a,b,c,N):
    j = 0
    N_in = 0 
    Monte_carlo_Volume.Vol = []
    X_in, Y_in,Z_in = [],[],[]
    Monte_carlo_Volume.X_out, Monte_carlo_Volume.Y_out,Monte_carlo_Volume.Z_out = [],[],[]
    #loop for finding M points inside elipsoid
    while(j<N):
        #random_points are generated
        x = random.random()
        y = random.random()
        z = random.random()
        x = -a + 2*a*x
        y = -b + 2*b*y
        z = -c + 2*c*z
        #finding the points which are enclosed within the eclipsoid
        if u(x,y,z,a,b,c) <=1:
            X_in.append(x)
            Y_in.append(y)
            Z_in.append(z)
            N_in +=1
        else:
            Monte_carlo_Volume.X_out.append(x)
            Monte_carlo_Volume.Y_out.append(y)
            Monte_carlo_Volume.Z_out.append(z)
        j+=1
    Monte_carlo_Volume.Vol = N_in*8*a*b*c/N
    Monte_carlo_Volume.error = abs(4*m.pi*a*b*c/3 - N_in*8*a*b*c/N)
    return(X_in,Y_in,Z_in)  

#3D plot for Monte_Carlo
from mpl_toolkits import mplot3d
def threeDplot(X ,Y , Z , s, t,x,y,z):
    fig = plt.figure(figsize=(9, 6))
    fig.suptitle(t)
    ax = plt.axes(projection='3d')
    # Data for three-dimensional scattered points
    ax.set_title('azim = 0 '+'elav = 45')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.view_init(0, 45)
    ax.set_xlim(-x,x)
    ax.set_ylim(-y,y)
    ax.set_zlim(-z,z)
    ax.scatter3D(X, Y, Z, c = X, cmap = 'gist_rainbow');
    plt.savefig('{}.pdf'.format(s))
    plt.show()
    


def plot_least_square(a,b,u,v):
    import numpy as np
    x = np.linspace(u,v,100)
    y = b*x+a
    plt.plot(x, y, '-r', label=r'$ln(\omega (t))$'+'='+str(round(b,7))+'x+'+str(round(a,7)))
    

"""
plot 3 list data
"""
def error_bar(X,Y,Z,x,y,s,A,name,n):
    plt.title(A) 
    plt.errorbar(X,Y,yerr = Z,marker = 'o', label = name)
    if isinstance(n, float) == True:
        plt.axhline(y=n,linewidth=2, color='r')
        plt.annotate(round(n,6),(0,n))
    plt.xlabel(str(x)+'---->')
    plt.ylabel(str(y)+'---->')
    plt.savefig(str(s)+'.pdf')
    
