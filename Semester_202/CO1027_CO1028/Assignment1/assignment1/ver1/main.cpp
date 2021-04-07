/*
    * Ho Chi Minh City University of Technology
    * Faculty of Computer Science and Engineering
    * Initial code for Assignment 1
    * Programming Fundamentals Spring 2021
    * Author: Nguyen Thanh Nhan
    * Date: 01.03.2021
*/

//The library here is concretely set, students are not allowed to include any other libraries.
#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

#include "mongol.h"

int readFile(const char *filename, int &NID, int &N1, int &N5, int &N7, string *&ID, string *&input1, string *&input2, string *&input3, string *&input4, string *&input5, string *&input6, string *&input7Matrix, string *&input7Str)
{
    // This function is used to read the input file,
    // DO NOT MODIFY THIS FUNTION
    // Because you do not need to submit this main file.
    ifstream myfile(filename);
    if (myfile.is_open())
    {

        //So this is how the reading process works
        //1.    string *tmp = new string: initalize a pointer of string, 
        //      which reads the input of the input.txt file and will be updated asd it goes on
        //2.    getline(myfile, *tmp): https://en.cppreference.com/w/cpp/string/basic_string/getline
        //      since tmp is a pointer, it actually get the address of the line and save it without harming the contents
        //      (You can use "std::cout << tmp << *tmp;" to see the address and it's contents)
        //3.    *variable* = stoi(*tmp): https://en.cppreference.com/w/cpp/string/basic_string/stol
        //      stoi has the same value as the guard, to check if the test cases doesn't contain anything "not integer"
        //      since all values that uses stoi is type int
        //4.    getline(myfile, array[num]);: same story as 2, 
        //      Another note: https://www.learncpp.com/cpp-tutorial/arrays-part-ii/ which should help you how arrays indices work
        //5.    delete tmp;: This is good practice on the new-delete combo.


        string *tmp = new string;
        getline(myfile, *tmp);
        NID = stoi(*tmp);  
        //NID = 3

        ID = new string[NID];
        //ID is array of string, with size of 3 
        //(note: NID = 3, so it can be changed)
        for (int i = 0; i < NID; i++)
        {
            getline(myfile, ID[i]); 
            //get 3 next line:
            //ID[0] = VUA123
            //ID[1] = abcdef
            //ID[2] = 12rff
        }

        getline(myfile, *tmp);
        N1 = stoi(*tmp);
        //N1 = 2

        input1 = new string[N1];
        for (int i = 0; i < N1; i++)
        {
            getline(myfile, input1[i]);
            //input1 is array of strings, with size of 2 
            //(note: N1 = 2, so it can be changed)
            //input1[0] = 10 1111 1010
            //input1[1] = 11 01 1010

        }

        input2 = new string[2];
        //input2 is array of strings, with size of 2 
        //(note: N1 = 2, so it can be changed)
        getline(myfile, input2[0]);
        //input2[0] = helloCSE, this is CSE ASM	
        getline(myfile, input2[1]);
        //input2[1] = CSE

        input3 = new string;
        //input3 is a string 
        getline(myfile, *input3);
        //input3 = 12 9 ULDULLD

        input4 = new string[2];
        //input2 is array of strings, with size of 2
        //(note: it is fixed)
        getline(myfile, input4[0]);
        //input4[0] = V(V(0))	
        getline(myfile, input4[1]);
        ////input4[1] = V(0)

        getline(myfile, *tmp);
        N5 = stoi(*tmp);
        //N5 = 3

        input5 = new string[N5];
        for (int i = 0; i < N5; i++)
        {
            getline(myfile, input5[i]);
            //input5 is array of strings, with size of 3
            //(note: N5 = 3, so it can be changed)
            //input5[0] = ABCDEF
            //input5[1] = GHEABC
            //input5[2] = HGCBAE
        }

        input6 = new string[10];
        //input6 is array of strings, with size of 10
        //(note: it is fixed)
        for (int i = 0; i < 10; i++)
        {
            getline(myfile, input6[i]);
            //input6[0] =     0010000000
            //input6[1] =     1100000000
            //input6[2] =     1011100000
            //input6[3] =     0002000000
            //input6[4] =     1000000000
            //input6[5] =     1100000000
            //input6[6] =     1101000000
            //input6[7] =     1100002000
            //input6[8] =     1100000001
            //input6[9] =     0000000000
        }

        getline(myfile, *tmp);
        N7 = stoi(*tmp);
        //N7 = 2

        input7Str = new string;
        getline(myfile, *input7Str);
        //input7Str = 2 12 1 1

        input7Matrix = new string[N7];
        for (int i = 0; i < N7; i++)
        {
            getline(myfile, input7Matrix[i]);
            //input7 is array of strings, with size of 2
            //(note: N7 = 2, so it can be changed)
            //input7[0] = 1 2 3 4
            //input7[1] = 2 3 4 5
        }

        delete tmp;
        return 1;
    }
    else
        return 0;
}

int main(int argc, const char *argv[])
{
    const char *filename = "testcase.txt";

    int NID = -1, N1 = -1, N5 = -1, N7 = -1;
    string *ID = nullptr;
    string *input1 = nullptr;
    string *input2 = nullptr;
    string *input3 = nullptr;
    string *input4 = nullptr;
    string *input5 = nullptr;
    string *input6 = nullptr;
    string *input7Matrix = nullptr;
    string *input7Str = nullptr;

    bool isRead = readFile(filename, NID, N1, N5, N7, ID, input1, input2, input3, input4, input5, input6, input7Matrix, input7Str);

    if (!isRead)
    {
        cout << "File cannot be read!";
        return 1;
    }
    else
    {
        cout << "Answer for task 1: " << readyForBattle(ID, NID, input1, N1) << endl;
        cout << "Answer for task 2: " << decode(input2[0], input2[1]) << endl;
        cout << "Answer for task 3: " << findRoute(ID, NID, input3) << endl;
        cout << "Answer for task 4: " << decodeVfunction(input4[0], input4[1]) << endl;
        cout << "Answer for task 5: " << findBetrayals(input5, N5) << endl;
        cout << "Answer for task 6: " << attack(input6) << endl;
        cout << "Answer for task 7: " << calculateNoOfWaitingDays(*input7Str, *input7Matrix, N7) << endl;
    }
    return 0;
}
