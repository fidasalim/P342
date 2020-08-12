/*
Q2) Create two vectors of type A=(a1,a2,a3) and B=(b1,b2,b3) with numbers of your choice (but
       not random numbers) in the code itself. Find A+B and A.B (dot product). (marks 3)
*/

#include <stdio.h>
int main() {
	int A[3][1] = {{2},{3},{4}};
	int B[3][1] = {{5},{6},{7}};
	int C[3][1];
	int D[3][1];
	int i,j;
	
	printf("The matrix A is [");
	for (i=0;i<3;i++){
		printf("[");
		for(j=0;j<1;j++){
			printf("%d",A[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
	
	printf("The matrix B is [");
	for (i=0;i<3;i++){
		printf("[");
		for(j=0;j<1;j++){
			printf("%d",B[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
	
	printf("The matrix A+B is [");
	for (i=0;i<3;i++){
		printf("[");
		for(j=0;j<1;j++){
			C[i][j] = A[i][j]+B[i][j];
			printf("%d",C[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
	
	printf("The matrix A.B is [");
	for (i=0;i<3;i++){
		printf("[");
		for(j=0;j<1;j++){
			D[i][j] = A[i][j]*B[i][j];
			printf("%d",D[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
    return 0;    
}


/*
Solution:
The matrix A is [[2],[3],[4],]
The matrix B is [[5],[6],[7],]
The matrix A+B is [[7],[9],[11],]
The matrix A.B is [[10],[18],[28],]
*/
