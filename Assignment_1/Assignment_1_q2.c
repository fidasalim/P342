//2) factorial n! say for n=10 or 15, check and trap negative integers, say for -5!

#include <stdio.h>
int main() {
	//defining the variables
    int n;
    int factorial = 1;
    int i;
	//calling for the input user
    printf("The factorial of the integer \'n\' can be found out\nWhat is the n value? : ");
    scanf("%d", &n); 
    //condition for positive and negative indeger
    if(n>0){
    	//loop 
    	for(i=1; i<n+1; i++){
    		factorial *= i;
		}
	}	
	//printing the sum
	printf("The factorial of the %d is %d\n", n, factorial);
    return 0;    
}
