/*Combination C(n,m) can be define as the following:

C(n,m) = 1, if m = 0 or m = n
C(n,m) = C(n-1, m) + C(n-1, m-1) if 0 < m < n
a/ Write a recursive function to calculate C(n,m)
b/ Write a C++ program promting 2 input integers M and N then call the written function to calculate C(N,M)

Input: 
2 integers M, N (0 ≤ M,N ≤ 25)

Output:
the value C(N,M)*/

#include <iostream>
using namespace std;
int permutation(int n, int m)
{
    if (m == n || n == 0 || m == 0) return 1;
    return permutation(n - 1, m) + permutation(n - 1, m - 1);
}
int main()
{
   int m, n;
   std::cin >> m >> n;
   cout<<permutation(n,m);
   return 0;
}