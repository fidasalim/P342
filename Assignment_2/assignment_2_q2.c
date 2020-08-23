/*
Q2) Create two vectors of type A=(a1,a2,a3) and B=(b1,b2,b3) with numbers of your choice (but
       not random numbers) in the code itself. Find A+B and A.B (dot product). (marks 3)
*/

#include <stdio.h>
int main() {
	float A[3] = {2,-3.5,4};
	float B[3] = {5,6,-7};
	float C[3];
	float dot;
	int i,j;
	
	printf("The vector A is [");
	for (i=0;i<3;i++){
		printf("%f,",A[i]);	
	}
	printf("]\n");
	
	printf("The vector B is [");
	for (i=0;i<3;i++){
		printf("%f,",B[i]);	
	}
	printf("]\n");
	
	printf("The vector A+B is [");
	for (i=0;i<3;i++){
		C[i] = A[i]+B[i];
		printf("%f,",C[i]);
	}
	printf("]\n");
	
	printf("The vector A.B is ");
	for (i=0;i<3;i++){
		dot += A[i]*B[i];
		
	}
	printf("%f.",dot);
    return 0;    
}


/*
Solution:
The vector A is [2.000000,-3.500000,4.000000,]
The vector B is [5.000000,6.000000,-7.000000,]
The vector A+B is [7.000000,2.500000,-3.000000,]
The vector A.B is -39.000000.
*/
