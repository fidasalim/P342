/*
Q1) Find the average distance between two points on a -- (marks 2+2)
    	(a) straight line made of discrete N (=6) points:	o---o---o---o---o---o
    	(b) 6 by 6 two-dimensional grid (no diagonal connections):
		o---o---o---o  …
		|   |   |   |  ...
		o---o---o---o  … etc
*/
#include <stdio.h>
int main() {
	//Q_1_a
	int line[6]; 
	int i,j;
	float sum_1,total_1,average_1 = 0;	
	for (i=0; i<6;i++){
		for (j=0;j<6;j++){
			if (i<j){
	            sum_1 += abs(i-j);
	            total_1 = total_1+1;
	    	}
		}
	}
	average_1 = sum_1/total_1;
	printf("The average distance between two points on a straight line made of discrete 6 points is %f.\n", average_1);
	
	int matrix[6][6];
	int x,y,a,b;
	float sum_2,average_2 = 0;
	float total_2 = 0;
	for (x=0; x<6;x++){
		for (y=0;y<6;y++){
			for (a=0;a<6;a++){
				for (b=0;b<6;b++){
					if(b>y){
						sum_2 += abs(x-a) + abs(y-b);
						total_2 ++;
					}
					if (a>x && b==y){
						sum_2 += abs(x-a);
						total_2 ++;
					}
				}
			}
		}
	}
	average_2 = sum_2/total_2;
	printf("The average distance between two points on a 6 by 6 two-dimensional grid (no diagonal connections) is %f.\n", average_2);
    return 0;    
}
/*
Solution:
The average distance between two points on a straight line made of discrete 6 points is 2.333333.
The average distance between two points on a 6 by 6 two-dimensional grid (no diagonal connections) is 4.000000.

*/
