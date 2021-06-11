/*Complete the following createPointer function. Function createPointer receives an integer n with value up to 5000 and a interger pointer p (p points to n)

Input:

Function createPointer receives an integer n (|n| ≤ 5000)

Output:

p satisfy the requirement.

(value b in function main is up to 5000)*/

#include<iostream>
using namespace std;
int *createPointer(int& n)
{
   int *p = &n;
   return p;
}
int main()
{
    int n,b;
    cin>>n>>b;
    int *p = createPointer(n);
    cout<<*p<<endl;
    n+=b;
    cout<<*p;
    return 0;
}