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
#plot_graph(R_rms,sqrtN,r'$\sqrt{N}$',r'$R_{rms}$',r'$R_{rms}$ vs $\sqrt{N}$','Rrms_vs_sqrt(N)')


"""
For N = 250,
 R_avg = 14.58718396929289
 R_rms = 16.138481294362972
 X_avg = -0.9750750195101945
 Y_avg = -2.889273355136563

For N = 500,
 R_avg = 19.037451361251666
 R_rms = 21.888897628178793
 X_avg = -0.665448868430901
 Y_avg = 0.9538170854479333

For N = 750,
 R_avg = 25.27372369239734
 R_rms = 28.16698116663954
 X_avg = 1.5578680119254193
 Y_avg = -2.4028073873168707

For N = 1000,
 R_avg = 27.527277962734075
 R_rms = 31.390455487671034
 X_avg = 1.74037664588639
 Y_avg = 2.0741633379664184

For N = 1250,
 R_avg = 31.225030668082322
 R_rms = 35.08884013148393
 X_avg = -6.175283752686287
 Y_avg = 6.486982894926171
"""