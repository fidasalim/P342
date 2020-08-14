/*
Q2) Create two vectors of type A=(a1,a2,a3) and B=(b1,b2,b3) with numbers of your choice (but
       not random numbers) in the code itself. Find A+B and A.B (dot product). (marks 3)
*/

#include <stdio.h>
int main() {
	float A[3][1] = {{2},{-3.5},{4}};
	float B[3][1] = {{5},{6},{-7}};
	float C[3][1];
	float D[3][1];
	int i,j;
	
	printf("The matrix A is [");
	for (i=0;i<3;i++){
		printf("[");
		for(j=0;j<1;j++){
			printf("%f",A[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
	
	printf("The matrix B is [");
	for (i=0;i<3;i++){
		printf("[");
		for(j=0;j<1;j++){
			printf("%f",B[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
	
	printf("The matrix A+B is [");
	for (i=0;i<3;i++){
		printf("[");
		for(j=0;j<1;j++){
			C[i][j] = A[i][j]+B[i][j];
			printf("%f",C[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
	
	printf("The matrix A.B is [");
	for (i=0;i<3;i++){
		printf("[");
		for(j=0;j<1;j++){
			D[i][j] = A[i][j]*B[i][j];
			printf("%f",D[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
    return 0;    
}


/*
Solution:
The matrix A is [[2.000000],[-3.500000],[4.000000],]
The matrix B is [[5.000000],[6.000000],[-7.000000],]
The matrix A+B is [[7.000000],[2.500000],[-3.000000],]
The matrix A.B is [[10.000000],[-21.000000],[-28.000000],]
*/
