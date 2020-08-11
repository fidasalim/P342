//Q1) Find the average distance between two points on a -- (marks 2+2)
//      (a) straight line made of discrete N (=6) points:	o---o---o---o---o---o
//    	(b) 6 by 6 two-dimensional grid (no diagonal connections):
//		o---o---o---o  …
//		|   |   |   |  ...
//		o---o---o---o  … etc

#include <stdio.h>
int main() {
	//Q_1_a
	int line[6];
	int i,j;
	float sum,total,average = 0;	
	for (i=0; i<6;i++){
		for (j=0;j<6;j++){
			if (i<j){
	            sum += abs(i-j);
	            total = total+1;
	    	}
		}
	}
	average = sum/total	;
	printf("The average distance between two points on a straight line made of discrete 6 points is %f", average);
    return 0;    
}
/*
Solution:
The average distance between two points on a straight line made of discrete 6 points is 2.333333
*/
