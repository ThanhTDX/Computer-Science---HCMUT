/*A 2D array F is defined by the following formular:

F[0][0] = 0
F[0][1] = F[1][0] = 1
If i ≥ 2, F[i][0] = F[i-1][0] + F[i-2][0]
If i ≥ 2, F[0][i] = F[0][i-1] + F[0][i-2]
If i, j ≥ 1, F[i][j] = F[i-1][j] + F[i][j-1]
For 2 input number x and y, find F[x][y]. The display value should be congruent modulo 109 +7. (I.e F[x][y] = 109 +7 the display result is 0)
Input:

Recursive function infinite2DArray has 2 input number x, y (0 ≤ x,y < 11)

Output:

Result satisfy the given requirements*/

#include<iostream>
#include<vector>
using namespace std;
long long infinite2DArray(int x, int y)
{
    if (x == 0)
    {
        if (y == 0) return 0;
        if (y == 1) return 1;
        else return infinite2DArray(0, y-1) + infinite2DArray(0, y-2);
    }
    else if (y == 0)
    {
        if (x == 0) return 0;
        if (x == 1) return 1;
        else return infinite2DArray(x-1, 0) + infinite2DArray(x-2, 0);
    }
    else return infinite2DArray(x-1, y) + infinite2DArray(x, y-1);
}
int main()
{
    int x,y;
    cin>>x>>y;
    cout<<infinite2DArray(x,y);
    return 0;
}