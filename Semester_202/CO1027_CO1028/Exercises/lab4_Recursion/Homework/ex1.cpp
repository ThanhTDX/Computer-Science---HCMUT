/*Write a recursive function to check if all elements in an array are unique (meaning there are no identical value element). I.e {1,2,3,4,5} is unique, and {1,2,3,2,5} is not unique because it has two element with value 2.

Input:

Function checkDuplicate will receive an integer array with value between (-109; 109) and the size in [1; 104]

Output:

Return true if there is no identical element, else return false*/

#include <iostream>
#include <vector>
using namespace std;
bool checkDuplicate(vector<int> ar)
{
    if ((int) ar.size() == 1) return true;
    int num = ar.back();
    ar.pop_back();
    for (const int &i: ar) 
    {
        if (i == num) return false;
    }
    return checkDuplicate(ar);
}
int main()
{
    int n;
    cin >> n;
    vector<int> ar(n);
    for (int i = 0; i < n; i++)
        cin >> ar[i];
    cout << checkDuplicate(ar);
    return 0;
}