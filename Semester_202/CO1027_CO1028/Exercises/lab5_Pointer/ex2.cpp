/*Write function readArray() which defined as following:

int** readArray()

This function read data from a 2D matrix 10x10. The elements will be inputted from keyboard from a[0][0] to a[9][9]. However if a[i][j] receives the value 0 then all a[i][k], j<k<10 will be automatically assigned 0, and program will continue at a[i+1][0] from keyboard. Function read Array will return a pointer to this 2D array.

Input:

the elements for the 2D array, each element is a positive integer with value up to 1000.

Output:

Pointer to the created 2D array*/

#include<iostream>
using namespace std;
int** readArray()
{
   int **arr = new int*[10];
   for (int Row = 0; Row < 10; Row++)
   {
        arr[Row] = new int[10];
        for (int Col = 0; Col < 10; Col++)
        {
            int num;
            std::cin >> num;
            if (num == 0)
            {
                for (; Col < 10; Col++)
                    arr[Row][Col] = num;
            }
            else arr[Row][Col] = num;
        }
   }
   return arr;
}
int main()
{
    int** ar = readArray();
    for(int i=0;i<10;i++)
    {
        for(int j=0;j<10;j++) cout<<ar[i][j]<<" ";
        cout<<endl;
    }
    for(int i=0;i<10;i++) delete[] ar[i];
    delete[] ar;
    return 0;
}

