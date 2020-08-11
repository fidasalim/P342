/*
Q3) Create 3x3 matrices M=(a11,a12 … a33) and N=(b11,b12, …, b33) with numbers of your
       choice (zeros, negatives and positives but not random numbers) in two separate files. Read
       the matrices from the files. Find M x A and M x N.
*/

#include <stdio.h>
#include "matrix_AB.c"
#include "matrix_M.c"
#include "matrix_N.c"
int main() {
	int i,j,k;
	//printing matrix A, M, N
	printf("The matrix A is [");
	for (i=0;i<A_row;i++){
		printf("[");
		for(j=0;j<A_col;j++){
			printf("%d",A[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
	
	printf("The matrix M is [");
	for (j=0;j<M_row;j++){
		printf("[");
		for(i=0;i<M_col;i++){
			printf("%d,",M[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
	
	printf("The matrix N is [");
	for (i=0;i<N_row;i++){
		printf("[");
		for(j=0;j<N_col;j++){
			printf("%d,",N[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
		
	//MxN
	int O[M_row][N_col];
	for (i=0;i<M_row;i++){
		for(j=0;j<N_col;j++){
			O[i][j] = 0;
		}	
	}
	
	printf("The matrix MxN is [");
	for(i=0;i<M_row;i++){
		printf("[");
		for(j=0;j<N_col;j++){
			for(k=0;k<M_col;k++){
				O[i][j]+= M[i][k]*N[k][j];	
			}
			printf("%d,",O[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
	
	//MxA
	int Q[M_row][A_col];
	for (i=0;i<M_row;i++){
		for(j=0;j<A_col;j++){
			Q[i][j] = 0;
		}	
	}
	
	printf("The matrix MxA is [");
	for(i=0;i<M_row;i++){
		printf("[");
		for(j=0;j<A_col;j++){
			for(k=0;k<M_col;k++){
				Q[i][j]+= M[i][k]*A[k][j];	
			}
			printf("%d,",Q[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
    return 0;    
}


/*
Solution:
The matrix A is [[2],[3],[4],]
The matrix M is [[1,4,0,],[2,-5,8,],[-3,6,9,],]
The matrix N is [[4,9,-7,],[0,6,2,],[9,-1,8,],]
The matrix MxN is [[-23,24,-27,],[70,0,10,],[81,39,88,],]
The matrix MxA is [[-4,],[17,],[60,],]
*/
