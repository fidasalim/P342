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
line=[0,0,0,0,0,0]
sum_1 = 0
total_1 = 0
print("The straight line made of discrete 6 points be {}.".format(line))
for i in range(len(line)):
    for j in range(len(line)):
            sum_1 += abs(i-j)
            total_1 = total_1+1
dist1_mean = sum_1/total_1
print("The average distance between two points on a straight line made of discrete 6 points is {} units.".format(dist1_mean)) 


row, col = 6, 6;
Matrix = [[0 for x in range(row)] for y in range(col)] 
sum_2 = 0
total_2 = 0
print("6 by 6 two-dimensional grid be {}.".format(Matrix))
for x in range(row):
    for y in range(col):
        for a in range(row):
                for b in range(col):
                        sum_2 += (abs(x-a)+abs(y-b))
                        total_2 = total_2+1    
dist2_mean = sum_2/total_2
print("The average distance between two points on a 6 by 6 two-dimensional grid (no diagonal connections) is {} units.".format(dist2_mean)) 

"""
Solution:
The straight line made of discrete 6 points be [0, 0, 0, 0, 0, 0].
The average distance between two points on a straight line made of discrete 6 points is 1.9444444444444444 units.
6 by 6 two-dimensional grid be [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]].
The average distance between two points on a 6 by 6 two-dimensional grid (no diagonal connections) is 3.888888888888889 units.
"""