/*A string is palindrome when it's reversed string identical to itself i.e: “ABCBA”, “RADAR”, “otto”, “i am ma i”, “C”.

Function  palindrome Check if an input string is Palindrome is given in the following part.


a/ Write a C++ program using while loop to read strings and using the said function to check if the input strings are palindrome. The loop end when the user input a string start with '*'.

b/ Write function palindromeRecursion using recursion to check if an input string is palindrome.

Input:

Strings s with lengths equal or less than 1000

Output:

each line return the value of function palindrome and palindromRecursion (refer to the example for detail)

*/

#include<iostream>
#include<string>
using namespace std;
bool palindrome(string strg)
{
    int len, k, j;
    len = strg.length();
    k = len/2;
    j = 0;
    bool palin = true;
    while ( j < k && palin)
       if (strg[j] != strg[len -1-j])
         palin = false;
       else
         ++ j;
   return (palin);
}
bool palindromeRecursion(string s)
{
    int sz = (int) s.size();
    if(sz <= 1) return true;
    if(s[0] != s[sz-1]) return false;
    else s = s.substr(1, sz - 2);
    return palindromeRecursion(s);
}
int main()
{
    while(1)
    {
        std::string word;
        std::getline(std::cin, word);
        if (word.substr(0,1) == "*") break;
        else std::cout << palindrome(word) << " " << palindromeRecursion(word);
    }
   return 0;
}


