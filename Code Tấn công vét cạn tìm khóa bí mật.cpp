#include <stdio.h>
#include <math.h>
#include <time.h>

/*Code tan cong Vet can (Phan tich n thanh tich 2 so p va q */
/*Nguyen Hai Dang */

int isPrime(int n) 
{
    int i;
    int m = (int) sqrt(n);
    for (i = 2; i <= m; i++) 
    {
        if(n % i == 0) 
            return 0;
    }
    return 1;
}

int main() 
{
    long long n,i;
    clock_t start, end;
    double time;
    printf("Enter number n = ");
    scanf("%lld", &n);
 
    printf("%ld = ", n);

    printf("Ket qua: ");
    start = clock();
    for (i = 2; i <= n; i++) 
    {
        while(n % i == 0) {
            printf("%d.", i);
            n /= i;
        }
    }
    end = clock();
    time = (double)(end - start)/ CLOCKS_PER_SEC;
    printf("\nThoi gian chay: %0.30f",time);
    printf("\n");
    return 0;
}
