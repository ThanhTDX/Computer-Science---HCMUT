/*Write function calcSum to find the sum of all element in an array.

Input:

Function calcSum input:

length of the input array,n;n<=1000
Each element from the input 1D array has value in (-1000; 1000)
Output:
Sum of all elements in the input 1D array*/

#include<iostream>
using namespace std;
int calcSum(int*ar, int n)
{
    int sum = 0;
    for (; n != 0; ar++, n--)
    {
        sum += *ar;
    }
    return sum;
}
int main()
{
    int n;
    cin>>n;
    int *ar= new int[n];
    for(int i=0;i<n;i++) cin>>ar[i];
    cout<< calcSum(ar, n);
    delete[] ar;
    return 0;
}