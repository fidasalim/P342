# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:23:29 2020

@author: fida
"""
import math as m

#introducing function and providing those function an attribute name
f1 = lambda x : m.log(x,m.e) - m.sin(x)
f2 = lambda x : -x - m.cos(x)
setattr(f1,'name','logx-sinx')
setattr(f2,'name','-x-cosx')
    
#single derivative function
def single_derivative(u,x):
    h = 0.01
    df1_x = (u(x+h)-u(x-h))/(2*h)
    return (df1_x)

#single derivative function
def double_derivative(f,x):
    h = 0.01
    df2_x = (f(x+2*h)+f(x-2*h)-(2*f(x)))/(4*(h*h))
    return (df2_x)

"""
BISECTION
"""
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
                a = float(input('New value for a-'))
                b = float(input('New value for b-'))
                bracketing_ab(u,a,b)
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
    title = '-Bisection_method'
    heading= '{}_({})'.format(title,u.name)
    #opening a file to save the error
    f = open(heading+'.txt',"w+")
    f.write(heading+'\nIteration\tAbsolute Error in (a-b)\n')
    #using bisection to get closer to the solution
    while(flag == True):
        f.write(str (i)+'\t\t'+str(abs(b-a))+'\n')
        c = (a+b)/2
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
        i=i+1
        #stop the loop if iteration exceeds 200
        if i >= 200:
            print("Choose another interval")
            flag = False 
    f.write(str (i)+'\t\t'+str(abs(b-a))+'\n')
    f.close()
    return((a+b)/2,'+-',abs(a-b)/2)

"""
REGULA_FALSI
"""       
def regula_falsi(u,p,q):
    a = p
    b = q
    flag = True
    i = 0
    falsi = [0]
    e = 1.0e-6
    title = '-Regula_Falsi'
    heading= '{}_({})'.format(title,u.name)
    #opening a file to save the error
    f = open(heading+'.txt',"w+")
    f.write(heading+'\nIteration\tAbsolute Error in c\n')
    #using regula_falsi get the solution
    #see if both the points are in the different side of f = 0
    if u(a)*u(b)<0:
        while(flag == True):
            m = (u(b)-u(a))/(b-a)
            c = b - (u(b)/m)
            falsi.append(c)
            if abs(falsi[i+1]-falsi[i])<e:
                flag = False
            elif u(a)*u(c) <0:
                b = c
            else:
                a = c
            if i>0:
                f.write(str (i)+'\t\t'+str(abs(falsi[i]-falsi[i-1]))+'\n')
            i+=1
            #stop the loop if iteration exceeds 200
            if i >= 200:
                print("Choose another interval")
                flag = False 
    #if a and b the points are in the same side of f = 0, then the function is called again
    else:
        print('You need to change values of a and b')
        a = float(input('New value for a-'))
        b = float(input('New value for b-'))
        regula_falsi(u,p,q)
    f.write(str (i)+'\t\t'+str(abs(falsi[i]-falsi[i-1]))+'\n')
    f.close()
    return(c,'+-',abs(falsi[i]-falsi[i-1]))
"""
NEWTON_RAPHSON
"""
def newton_raphson(u,a):
    x = a
    flag = True
    i = 1
    x_values = [x]
    e = 1.0e-6
    title = '-Newton_Raphson'
    heading= '{}_({})'.format(title,u.name)
    f = open(heading+'.txt',"w+")
    f.write(heading+'\nIteration\tAbsolute Error in x_values\n')
    #using newton_raphson get the solution
    while(flag == True):
        du = single_derivative(u,x)
        x = x - u(x)/du
        x_values.append(x)
        if abs(x - x_values[i-1])<e:
            f.write(str (i)+'\t\t'+str(abs(x - x_values[i-1]))+'\n')
            flag = False  
        else:
            f.write(str (i)+'\t\t'+str(abs(x - x_values[i-1]))+'\n')
        i+=1
        #stop the loop if iteration exceeds 200
        if i >= 200:
            print('You need to change values of x_0')
            a = float(input('New value for x_0-'))
            flag = None
    #function called again if we havent got the solution
    if flag == None:
        newton_raphson(u,a)
    #return solution
    else:
        f.close()
        return(x,'+-',abs(x - x_values[i-1]))
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
                print("Choose another x_0")
                x_0 = float(input('Which is the x_0 value?'))
                flag = None
            d1 = g + m.sqrt((n-1)*(n*h-pow(g,2)))
            d2 = g - m.sqrt((n-1)*(n*h-pow(g,2)))
            a = n/max(d1,d2)
            x = x-a
            i+=1 
            if abs(a)<e :
                R.append(x)
                flag = False
            else:            
                continue
    #calling the function again if something went wrong
    if flag == None:
        laguerres_method(x_0,A ,R)
        
#synthetic division
def synthetic_division_method(A = [], R = []):
    B = [A[0]]
    for i in range(1,len(A)):
        b =A[i]+(R[-1]*B[i-1])
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
        S = synthetic_division_method(S,R) 
    return(R)
    
