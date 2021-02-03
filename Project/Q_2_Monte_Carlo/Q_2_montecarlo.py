# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 19:43:46 2021

@author: fida
"""
from lib_project import *
import math as m

frac_error,Volume= [],[]
#lis for defining the step_size
N_list = [100,500,1000,2000,5000,10000,15000,20000,30000,40000]
for n in N_list:
    Monte_carlo_Volume(f1,1,1.5,2,n)
    Vol = Monte_carlo_Volume.Vol
    Error = Monte_carlo_Volume.error
    Volume.append(Vol)
    #finding fractional error
    frac_error.append((Error/Vol))

X_in, Y_in, Z_in = Monte_carlo_Volume(f1,1,1.5,2,20000)
#threeDplot(X_in ,Y_in , Z_in , 'Monte_Carlo_Elipsoid','Elipsoid_using_Monte_Carlo_for_N=10000',1,1.5,2)
