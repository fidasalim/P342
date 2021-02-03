# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 19:56:54 2021

@author: fida
"""


import math as m
import matplotlib.pyplot as plt
import random

#defining functions
f1 = lambda x,y,z,a,b,c : (pow(x/a,2) +pow(y/b,2) +pow(z/c,2))
                           
    
#random_walk
def random_walk(N,k,n):
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
    return(X,Y,R,R_2,X_d,Y_d)
 
    
"""
MOnte_Carlo
"""

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
