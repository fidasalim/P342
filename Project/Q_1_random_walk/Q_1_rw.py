# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 12:33:19 2021

@author: fida
"""
from library_project import *
import math as m


N = [250,500,750,1000,1250]
k = 100
R_avg = []
R_rms = []
X_avg = []
Y_avg = []
sqrtN = []
for i in N:
    X,Y,R,R_2, X_d, Y_d = random_walk(i,k,5)
    #appending R_avg, R_rms, X_avg, Y_avg, sqrtNas a list
    R_avg.append(R/k)
    R_rms.append(m.sqrt(R_2/k))
    X_avg.append(X_d/k)
    Y_avg.append(Y_d/k)
    sqrtN.append(m.sqrt(i))
    print('For N = {},\n R_avg = {}\n R_rms = {}\n X_avg = {}\n Y_avg = {}\n'.format(i,R_avg[-1],R_rms[-1],X_avg[-1],Y_avg[-1]))
plot_graph(R_rms,sqrtN,'sqrt(N)','R_rms',"R_rms vs sqrt(N)")


"""
For N = 250,
 R_avg = 13.97573633041244
 R_rms = 15.716282244225056
 X_avg = -0.2695568616450592
 Y_avg = -0.8279260044697874

For N = 500,
 R_avg = 19.488739506172475
 R_rms = 22.410213986266
 X_avg = -0.9771608453743192
 Y_avg = 2.371482631893408

For N = 750,
 R_avg = 22.930120025705904
 R_rms = 25.13800556950629
 X_avg = 0.11827407489061638
 Y_avg = -3.3903116937633486

For N = 1000,
 R_avg = 25.47938801809812
 R_rms = 29.06061093528139
 X_avg = -0.8396761633560526
 Y_avg = -1.2649561965416345

For N = 1250,
 R_avg = 29.37007273592605
 R_rms = 32.986663749964926
 X_avg = -2.5180623864514735
 Y_avg = -1.0881437422183702
"""