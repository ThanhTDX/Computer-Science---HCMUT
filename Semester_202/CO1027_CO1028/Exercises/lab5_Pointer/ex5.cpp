/*Write a function getValueAtIndex receives a pointer which pointing to the first index of a 1D array, size of the array, and an index k. Function getValueAtIndex return a pointer which pointing to the kth element of the input array. If there is no kth element, return NULL

Input:

int pointer ar pointing to the first index of the 1D array

positive integer n as size, n is up to 5000

Index k in (-5000 < k < 5000000)

Output:

Pointer satisfy the requirement*/

#include<iostream>
using namespace std;
int * getValueAtIndex(int * arr, int n, int k)
{
    int *kNum = arr;
    if (k > n) return NULL;
    while (k != 0)
    {
        kNum++;
        k--
    }
    return kNum;
}
int main()
{
    int n;
    cin>>n;
    int *ar = new int[n];
    for(int i=0;i<n;i++) cin>>ar[i];
    int k;
    cin>>k;
    int *p = getValueAtIndex(ar,n,k);
    if(p== NULL) cout<<"NULL pointer";
    else cout<< *p;
    delete[] ar;
    return 0;
}