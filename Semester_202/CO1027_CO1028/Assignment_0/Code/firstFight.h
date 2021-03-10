/*
    * Ho Chi Minh City University of Technology
    * Faculty of Computer Science and Engineering
    * Initial code for Assignment 0
    * Programming Fundamentals Spring 2021
    * Author: Nguyen Thanh Nhan
    * Date: 08.02.2021
*/

//The library here is concretely set, students are not allowed to include any other libraries.
#ifndef firstFight_h
#define firstFight_h

#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <fstream>

using namespace std;

////////////////////////////////////////////////////////////////////////
///STUDENT'S ANSWER BEGINS HERE
///Complete the following functions
///DO NOT modify any parameters in the functions.
////////////////////////////////////////////////////////////////////////
void reBalance(int& HP, int& M)
{
    if (HP > 1000) HP = 1000;
    if (HP < 0) HP = 0;
    if (M > 1000) M = 1000;
    if (M < 0) M = 0;
}
bool lastDigitPrime(int num)
{
    if (num == 2 ||
        num == 3 ||
        num == 5 ||
        num == 7) return true;
    else return false;
}
int getReady(int& HP, const int& ID, int& M, const int& E1)
{
    //Complete this function to gain point on task 1
    reBalance(HP, M);   //Setting numbers in range
    if (E1 >= 100 && E1 <= 199)     //Condition 4.1.1
    {
        //Initially, I thought of using struct for WP1 and WP2
        //But later on, since there's only 2 variables
        //It's faster to just declare each an array
        int WP1[2] = {300, 50};
        int WP2[2] = {200, 25};
        switch(ID)  //Check the leader
        {
        case 0:     //No leader
            {
                if ((E1 - 100)%64 >= HP%100) break;
                if (HP >= 500 && M%2 == 1 && M > WP1[0])
                {
                    HP += WP1[1];
                    M -= WP1[0];
                }
                if (M%2 == 0 && M >= WP2[0])
                {
                    HP += WP2[1];
                    M -= WP2[0];
                }
                break;
            }
        case 1:     //King
            {
                HP += WP1[1] + WP2[1];
                break;
            }
        case 2:     //Landlord
            break;
        }
        reBalance(HP, M);
        return HP + M;
    }

    if (E1 >= 200 && E1 <= 299)     //Condition 4.1.2
    {
        int MG[2] = {190 + 5*(E1%4), 5 + 2*(E1%4)};
        //Thinking MG as MG0, MG1, MG2, MG3 is easier
        //Since you can compare it to E1%4
        if ((M%2) != (E1%2) || ID == 1 || ID == 2)
        {
            if (M >= MG[0])
            {
                M -= MG[0];
                HP += MG[1];
            }
        }
        reBalance(HP, M);
        return HP + M;
    }

    if (E1 >= 300 && E1 <= 399)     //Condition 4.1.3
    {
        //This is straight-forward, no comment needed
        int a = E1%100;
        if (lastDigitPrime(a)) a *= 2;
        else a = 1;
        int dao[2] = {300, static_cast<int>((HP*(100 + a) - 1)/100)};
        int thuong[2] = {500,  static_cast<int>((HP*(100 + 2*a) - 1)/100)};

        if (HP >= 600)
        {
            if (lastDigitPrime(HP%10) && M >= thuong[0])
            {
                M -= thuong[0];
                if (ID == 1) HP += 200;
                else HP += thuong[1];
            }
            else if (M >= dao[0])
            {
                M -= dao[0];
            }
        }
        reBalance(HP, M);
        return HP + M;
    }

    if (E1 >= 400 && E1 <= 499)     //Condition 4.1.4
    {
        //There are many solution to round numbers up
        //Best is to have test cases to find out which is THE best solution
        if (E1%5 == 0) HP = (HP*9-1)/10 + 1;
        reBalance(HP, M);
        return HP + M;
    }

    if (E1 == 500)     //Condition 4.1.5
    {
        HP = (HP*3-1)/4+1;
        M = (M*3-1)/4+1;
        reBalance(HP, M);
        return HP + M;
    }

    else return -999;
}
int firstBattle(int& HP1, int& HP2, const int& ID1, const int& ID2, const int& E2){
    //Complete this function to gain point on task 2
    if (E2 >= 100 && E2 <= 199)     //Condition 4.3.1
    {
        HP1 = (HP1*11-1)/10 + 1;
        HP2 = (HP2*13-1)/10 + 1;
        reBalance(HP1,HP2);
    }

    else if (E2 >= 200 && E2 <= 299)     //Condition 4.3.2
    {
        HP1 = (HP1*17-1)/10 + 1;
        HP2 = (HP2*12-1)/10 + 1;
        reBalance(HP1,HP2);
    }

    else if (E2 >= 300 && E2 <= 399)     //Condition 4.3.3
    {
        HP1 += (E2 < 350)? 30 : E2%100;
        reBalance(HP1,HP2);
        //Wait, Error?
    }

    else if (E2 >= 400 && E2 <= 499)     //Condition 4.3.4
    {
        HP1 = (((HP1*13-1)/10 + 1)-1)/2 + 1;
        HP2 = (HP2*8-1)/10 + 1;
        reBalance(HP1,HP2);
    }

    else return -999;
    int muy = ((2*HP1*HP2) - 1)/(HP1+HP2) + 1;
    int aHP1 = HP1 - abs(HP2 - muy);
    int aHP2 = HP2 - abs(HP1 - muy);
    if ((ID1 == 0 && ID2 != 0) || aHP1 < aHP2)
    {
        HP1 = (aHP1*4-1)/5 + 1;     //Condition 4.3.5
        return -1;
    }

    if ((ID1 != 0 && ID2 != 0) || aHP1 == aHP2)
    {
        HP1 = (HP1*4-1)/5 + 1;
        return 0;
    }

    if ((ID1 != 0 && ID2 == 0) || aHP1 > aHP2)
    {
        HP1 = (aHP1*4-1)/5 + 1;
        return 1;
    }
    else return -999;
}

int secondBattle(int& HP1, int& HP2, const int& ID1, const int& ID2, const int& E3){
    //Complete this function to gain point on task 3
    HP1 = (HP1*14-1)/10 + 1;
    HP2 = (HP2*16-1)/10 + 1;
    if (ID1 == 1) HP1 *= 2;
    if (ID2 != 2) HP2 = (HP2*95-1)/100 + 1;

    if (E3 >= 100 && E3 <= 199);     //Condition 4.2.2
    else if (E3 >= 200 && E3 <= 299)     //Condition 4.2.2
    {
        reBalance(HP1,HP2);
        return 0;
    }
    else return -999;
    reBalance(HP1,HP2);

    int muy = ((2*HP1*HP2) - 1)/(HP1+HP2) + 1;
    int aHP1 = HP1 - abs(HP2 - muy);
    int aHP2 = HP2 - abs(HP1 - muy);

    if ((ID1 == 0 && ID2 != 0) || aHP1 < aHP2)
    {
        return -1;
    }

    if ((ID1 != 0 && ID2 != 0) || aHP1 == aHP2)
    {
        return 0;
    }

    if ((ID1 != 0 && ID2 == 0) || aHP1 > aHP2)
    {
        if (ID2 != 2) HP2 = aHP2;
        return 1;
    }
    else return -999;
}

int finalBattle(int& HP1, int& HP2, const int& , const int& ID2, const int& E4){
    //Complete this function to gain point on task 4
    if (E4 >= 100 && E4 <= 199)     //Condition 4.5.1
    {
        if (ID2 != 0) HP2 = (HP2*7-1)/10 + 1;
        else HP2 = (HP2*9-1)/10 + 1;
        reBalance(HP1, HP2);
        return 0;
    }

    else if (E4 >= 200 && E4 <= 299)     //Condition 4.5.2
    {
        HP2 = 0;
        return 1;
    }
    else return -999;
}
////////////////////////////////////////////////
///END OF STUDENT'S ANSWER
////////////////////////////////////////////////
#endif /* firstFight_h */
