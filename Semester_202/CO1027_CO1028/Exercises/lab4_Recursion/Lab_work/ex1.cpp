/*A function to find Greatest Common Divisor (GCD) of 2 positive integer can be written using basic loop or resursion. Write function gcdRecursion to find GCD using recursion and gcdIteration to find GCD using loop

Input:

2 integers p and q (1 ≤ p,q < 109 ).

Output:

The value of function  gcdRecursion and function  gcdIteration respectively*/

#include<iostream>
using namespace std;
int gcdRecursion(int p, int q)
{
    if (p == 0) return q;
    if (q == 0) return p;
    if (p == q) return p;
    if (p  > q) return gcdRecursion(p - q, q);
    else return gcdRecursion(p, q - p);
}
int gcdIteration(int p, int q)
{
   while (1)
   {
        if (p == 0) return q;
        if (q == 0) return p;
        if (p == q) return p;
        if (p > q) p = p - q;
        else q = q - p;
   }
}
int main()
{
    int p,q;
    cin>>p>>q;
    cout<<gcdRecursion(p,q)<< " "<<gcdIteration(p,q);
    return 0;
}
