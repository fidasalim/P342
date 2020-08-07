//3) sum over 1+1/2 + 1/3 + ... till the sum does not change by more than 0.001

#include <stdio.h>
int main() {
	//defining the variables
    double n = 1;
    double total = 0;
	//loop 
	while ((1/n) >= 0.001){
		total += (1/n);
		printf("%lf - %lf \n",n,total);
		n++ ;
	}	
	//printing the quote
	printf(" The sum over 1+1/2 + 1/3 + ... till the sum does not change by more than 0.001 is for the %dth sum %lf \n",(int)n-1,total);
    return 0;    
}
