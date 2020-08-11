# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:31:09 2020

@author: fida

Q1) Find the average distance between two points on a -- (marks 2+2)
        (a) straight line made of discrete N (=6) points:	o---o---o---o---o---o
    	(b) 6 by 6 two-dimensional grid (no diagonal connections):
		o---o---o---o  …
		|   |   |   |  ...
		o---o---o---o  … etc

"""
line=[1,2,3,4,5,6]
dist=[]
summ = 0
total = 0
for i in range(len(line)):
    for j in range(len(line)):
        if i<j:
            summ += abs(i-j)
            total=total+1
print(summ, total)
dist_mean = summ/total
print("The average distance between two points on a straight line made of discrete 6 points is {}".format(dist_mean)) 

"""
Solution:
The average distance between two points on a straight line made of discrete 6 points is 2.3333333333333335
"""

row, col = 6, 6;
Matrix = [[0 for x in range(row)] for y in range(col)] 
dist_1 = []
print(Matrix)
for x in range(row):
    for y in range(col):
        for a in range(row):
                for b in range(col):
                    if b>y:
                        dist_1.append(abs(x-a)+abs(y-b))
print(dist_1)
