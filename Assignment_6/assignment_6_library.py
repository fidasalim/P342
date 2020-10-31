# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 20:42:37 2020

@author: fida
"""


import math as m
import random 

#introducing function and providing those function an attribute name
f2 = lambda x : x/(1+x)
f3 = lambda x : m.exp(-m.pow(x,2))
f4 = lambda x : 4/(1+(x*x))
setattr(f2,'name','x/(1+x)')
setattr(f3,'name','exp(-x^2)')
setattr(f4,'name','4/(1+x^2)')

#single derivative function
def single_derivative(u,x):
    h = 0.01
    df1_x = (u(x+h)-u(x-h))/(2*h)
    return (df1_x)

#double derivative function
def double_derivative(u,x):
    h = 0.01
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
"""
setattr(Midpoint_method,'name','Midpoint')
setattr(Trapezoidal_method,'name','Trepizoidal')
setattr(Simpson_method,'name','Simpson_method')

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


def Monte_carlo(u,a,b,n):
    j = 1
    Monte_Carlo = []
    STD = []
    N_list = []
    while(j<=3000):
        N = j*n
        i = 1
        suM = 0 
        suM2 = 0
        while(i<=N):
            x = random.random()  
            x = a + (b-a)*x
            suM += u(x)
            suM2 += u(x)*u(x)
            i+=1
        sigma = m.sqrt((suM2/N)-m.pow(suM/N,2))
        STD.append(sigma)
        M_C = (b-a)*suM/N 
        Monte_Carlo.append(M_C)
        N_list.append(N)
        j += 1
    