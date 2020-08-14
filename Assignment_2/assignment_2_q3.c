#include <stdio.h>
int main(){
	int i,j,k;
	    
	//reading file A.txt
	FILE *A_matrix;
	A_matrix=fopen("A.txt", "r");
	float A[3][1]={0.0};
    	printf("The matrix A is [");
    	for(i=0 ;i<3; i++){
    		printf("[");
        	for(j=0; j<1; j++){
            		fscanf(A_matrix, "%f%*c",&A[i][j]);
            		printf("%f",A[i][j]);
        	}
        	printf("],");
    	}
    	printf("]\n");
    
    	//reading file M.txt 
    	FILE *M_matrix;
	M_matrix=fopen("M.txt", "r");
    	float M[3][3]={0.0};
    	printf("The matrix M is [");
   	for(i=0 ;i<3; i++){
    		printf("[");
        	for(j=0; j<3; j++){
           		fscanf(M_matrix, "%f%*c%*",&M[i][j]);
            		printf("%f,",M[i][j]);
        	}
        	printf("],");
	}
	printf("]\n");
	
	//reading file N.txt 
    	FILE *N_matrix;
	N_matrix=fopen("N.txt", "r");
	float N[3][3]={0.0};
    	printf("The matrix N is [");
    	for(i=0 ;i<3; i++){
    		printf("[");
        	for(j=0; j<3; j++){
            		fscanf(N_matrix, "%f%*c%*",&N[i][j]);
            		printf("%f,",N[i][j]);
        	}
       		 printf("],");
	}
	printf("]\n");
	
	//MxN
	float O[3][3] = {0.0};

	printf("The matrix MxN is [");
	for(i=0;i<3;i++){
		for(j=0;j<3;j++){
			for(k=0;k<3;k++){
				O[i][j]+= M[i][k]*N[k][j];	
			}
			printf("%f,",O[i][j]);
		}	
	}
	printf("]\n");
	
	//MxA
	float Q[3][1] = {0.0};
	
	printf("The matrix MxA is [");
	for(i=0;i<3;i++){
		printf("[");
		for(j=0;j<1;j++){
			for(k=0;k<3;k++){
				Q[i][j]+= M[i][k]*A[k][j];	
			}
			printf("%f,",Q[i][j]);
		}
		printf("],");	
	}
	printf("]\n");
	
    return 0; 	
}
/*
The matrix A is [[2.000000],[-3.500000],[4.000000],]
The matrix M is [[1.000000,2.000000,-3.000000,],[4.000000,-5.000000,6.000000,],[0.000000,8.000000,9.000000,],]
The matrix N is [[4.000000,9.000000,-7.000000,],[0.000000,6.000000,2.500000,],[9.000000,-1.000000,8.000000,],]
The matrix MxN is [-23.000000,24.000000,-26.000000,70.000000,0.000000,7.500000,81.000000,39.000000,92.000000,]
The matrix MxA is [[-17.000000,],[49.500000,],[8.000000,],]
*/   
