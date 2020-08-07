//1_a) add 1+2+3+ ... 100 WITHOUT using the formula n(n+1)/2
//1_b) add 1+2+3+ ... n WITHOUT using the formula n(n+1)/2

#include <stdio.h>
int main() {
	//defining the variables
    int n;
    int total1, total2 = 0;
    int i;
//1_a) add 1+2+3+ ... 100 WITHOUT using the formula n(n+1)/2
    //loop 
    for(i=0; i<101; i++){
    	total1 += i;
	}
	//printing the sum
	printf("Sum of the first 100 natural number is %d\n",total1);
	
//1_b) add 1+2+3+ ... n WITHOUT using the formula n(n+1)/2
    //calling for the input user
    printf("The sum of first n natural number can be found out\nWhat is the n value? : ");
    scanf("%d", &n); 
    //loop 
    for(i=0; i<n+1; i++){
    	total2 += i;
	}
	//printing the sum
	printf("%d\n",total2);
    return 0;    
}
