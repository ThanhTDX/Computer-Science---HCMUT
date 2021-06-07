/*The normal way to calculate ab is to loop b times the accumulate product of a (a*a*a*...*a). However, that method is not effective in case b is a really large number. Therefore, propose a more effective method to calculate a to the power of b using recursion .

Hint: to calculate a4 instead of calculate a*a*a*a you can calculate c = a2. Then calculate c*c.

Input:

Function superPow receive 2 inputs number a,b (1 ≤ a,b ≤ 1015)

Output:

Function superPow return (ab mod (109+7)). Properties of mod (a*b)%c = (a%c * b%c)%c

*/

#include<iostream>
using namespace std;

#define num 1000000007
long long superPow(long long a, long long b)
{
    long long int ans = 1;
    a = a % num;
    for(long long int powa = a; b ; b = b >> 1)
    {
        if(b & 1) ans = (ans * powa) % num;
        powa = (powa * powa) % num;
    }
    return ans;
}
int main()
{
    long long a,b;
    cin>>a>>b;
    cout<<superPow(a,b);
    return 0;
}