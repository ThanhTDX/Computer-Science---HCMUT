/*Write the function findMax to find the maximum value from a 1D array.

Input:

Function findMax  receives:

size n of the 1D array, n's value is up to 1000
the 1D array in which each element's value in (-1000; 1000)
Output:
Maximum of the given 1D array*/

#include<iostream>
using namespace std;
int findMax(int*ar, int n)
{
   int *ptr = ar;
   int maxNum = *ptr;
   while (n != 0)
   {
       if (maxNum < *ptr) maxNum = *ptr;
       ptr++;
       n--;
   }
   return maxNum;
}
int main()
{
    int n;
    cin>>n;
    int *ar= new int[n];
    for(int i=0;i<n;i++) cin>>ar[i];
    cout<< findMax(ar, n);
    delete[] ar;
    return 0;
}