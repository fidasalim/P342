# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 11:11:55 2020

@author: fida
"""


import math as m
#defining functions and providind name to functions
f1a = lambda y,x : y*m.log(y)/x
f1b = lambda y,x : 6 - (2*y/x)
f2 = lambda z,y,x : -z + 1 - x
f3 = lambda z,y,x : z + 1
setattr(f1a,'name','dy/dx=ylog(y)/x')
setattr(f1b,'name','dy/dx=6-(2y/x)')
setattr(f2,'name','d2y/dx2+dy/dx=1-x')
setattr(f3,'name','d2y/dx2=dy/dx+1')

import matplotlib.pyplot as plt
import numpy as np   
def analytic_function(u,x_0,x_n):
    if u == f1a:
        x = np.linspace(x_0,x_n,100)
        y = np.exp(x/2)
        label = 'y = exp(x/2)'
    if u == f1b:
        x = np.linspace(x_0,x_n,100)
        y = 2*x - 45/(x*x)
        label = 'y = 2*x - 45*x^2'
    if u == f2:
        x = np.linspace(x_0,x_n,100)
        y = 1 + 1*np.exp(-x)-(x*x)/2 + 2*x
        label = 'y = -1+exp(-x)-x^2/2 +2x)'
    if u == f3:
        x = np.linspace(x_0,x_n,100)
        y = 2*np.exp(x)-x-1
        label = 'y = 2e^x-x-1'
    return(x,y,label)

def tabular_data(p,x,X=[],Y=[]):
    f = open(x+'.txt',"w+")
    if p =='p':
        for i in range(len(Y)):
            f.write(str (X[i])+'\t\t'+str(Y[i])+'\n')
            print(str (X[i])+'\t\t'+str(Y[i])+'\n')
    else:
         for i in range(len(Y)):
            f.write(str (X[i])+'\t\t'+str(Y[i])+'\n')
    f.close()

def plot_curve(u,t,name):
    plt.xlabel('x')
    plt.ylabel('y(x)')
    if t == 'limx':
        lx1 = float(input('limit x axis from x1 = '))
        lx2 = float(input('to x2 = '))
        plt.xlim(lx1,lx2)
    if t == 'limy':
        ly1 = float(input('limit y axis from y1 = '))
        ly2 = float(input('to y2 = '))
        plt.ylim(ly1,ly2)
    if t == 'limxy':
        lx1 = float(input('limit x axis from x1 = '))
        lx2 = float(input('to x2 = '))
        plt.xlim(lx1,lx2)
        ly1 = float(input('limit y axis from y1 = '))
        ly2 = float(input('to y2 = '))
        plt.ylim(ly1,ly2)
    else:
        None
    plt.title(u.name) 
    plt.legend()
    plt.savefig(name+'.pdf', dpi = 300)
    plt.show()
    
#Explicit_Euler_method     
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


                

#Runge_Kutta4_method_for second order DE
def Runge_Kutta4_method_2_O(u,h,x_0,x_n,y_0,z_0):
    X = [x_0]
    Y = [y_0]
    x = x_0
    y = y_0
    z = z_0
    N = int((x_n - x_0)/h)
    for n in range(N):
        #defining k1,k2,k3,k4 for all the y and dy/dx
        k1y = h*z
        k1z = h*u(z,y,x)
        k2y = h*(z + k1z/2)
        k2z = h*u(z+ k1z/2,y + k1y/2,x + h/2)
        k3y = h*(z + k2z/2) 
        k3z = h*u((z+k2z/2),(y + k2y/2),(x + h/2))
        k4y = h*(z + k3z)
        k4z = h*u((z+k3z),(y + k2y),(x + h))
        x = x + h
        #new y and new dy/dx on a small increment of dx = h
        y = y + 1/6*(k1y+(2*k2y)+(2*k3y)+k4y)
        z = z + 1/6*(k1z+(2*k2z)+(2*k3z)+k4z)
        X.append(x)
        Y.append(y)
    return(X,Y)

#shooting method along with RK4
def shooting_method(u,N,a,b,y_a,y_b):
        #defining slope1
        g_1 = float(input('Guess_1 the slope at y({}):'.format(a)))
        M,N1 = Runge_Kutta4_method_2_O(u,N,a,b,y_a,g_1)
        #coorecting slope 1 to ve less than 0
        while (round(N1[-1],5) >y_b):
            print('The guess a smaller slope')
            g_1 = float(input('Guess_1 the slope at y({}):'.format(a)))
            M,N1 = Runge_Kutta4_method_2_O(u,N,a,b,y_a,g_1)   
        if round(N1[-1] - y_b,5)!= 0:
            #defining slope 2 
            g_2 = float(input('Guess_2 the slope at y({}):'.format(a)))
            M,N2 = Runge_Kutta4_method_2_O(u,N,a,b,y_a,g_2)
            #correcting slope to be greater than 0
            while (round(N2[-1],5)<y_b):
                print('The guess a larger slope')
                g_2 = float(input('Guess_2 the slope at y({}):'.format(a)))
                M,N2 = Runge_Kutta4_method_2_O(u,N,a,b,y_a,g_2)
            #lagrange_interpolation
            l = g_1 + (g_2 - g_1)*(y_b-N1[-1])/(N2[-1]-N1[-1])
            print('Using langrange extrapolation, the slope at y({}) is {}\n'.format(a,l))
            M,N1 = Runge_Kutta4_method_2_O(u,N,a,b,y_a,l)
        return(M,N1)
