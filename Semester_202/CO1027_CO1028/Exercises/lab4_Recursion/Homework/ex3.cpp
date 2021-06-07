/*Fibonacci is an interesting sequence. Write a recursive function to calculate the nth Fibonacci number. Where:
Fibo(0) = 0
Fibo(1) = 1
Fibo(n) =  Fibo(n-1) + Fibo(n-2) if n ≥ 2
Input:
integer n ( 0 ≤ n ≤ 29)
Output:
The nth fibonacci value*/

#include <iostream>
using namespace std;
int fibonacci(int n)
{
    if (n == 0) return 0;
    if (n == 1) return 1;
    else return fibonacci(n-1) + fibonacci(n-2);
}
int main()
{
    int n;
    cin >> n;
    cout << fibonacci(n);
    return 0;
}