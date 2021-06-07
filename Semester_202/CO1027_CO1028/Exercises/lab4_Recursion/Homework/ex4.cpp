/*Write a function recursiveSearch receive an input an length N array, and a value M. Function recursiveSearch return the first index that has value M in the input array (assume the index is k) and remove this index k element from the array. If no value M element found return -1

Input:

function recursiveSearch receive the following input:

length of the array, N (0 ≤ N ≤ 108)
The length N arr with each element in (0; 109)
number M (0 < M < 109)
Output:
Function recursiveSearch return as the problem requires*/

#include<iostream>
using namespace std;
int recursiveSearch(int& n , int m, int arr[], int index)
{
   //TODO
   if (index == n || n == 0) return -1;
   if (arr[index] == m) 
   {
       for(int i = index; i < n; i++)
       {
           arr[i] = arr[i+1];
       }
       n--;
       return index;
   }
   else return recursiveSearch(n, m, arr, ++index);
}
int n,m;
int main()
{
    cin>>n>>m;
    int arr[n];
    for(int i=0;i<n;i++) cin>>arr[i];
    cout<<recursiveSearch(n,m,arr,0)<<endl;
    for(int i=0;i<n;i++) cout<< arr[i] <<" ";
    return 0;
}