//
// Created by Nhan Nguyen on 01/03/2021.
//
#ifndef MONGOL_H
#define MONGOL_H

// The library here is concretely set, students are not allowed to include any other libraries.

string readyForBattle(const string ID[], const int NID, const string input1[], const int N1);
int decode(const string A, const string B);
string findRoute(const string ID[], const int NID, const string input3[]);
string decodeVfunction(const string A, const string B);
string findBetrayals(const string input5[], const int N5);
int attack(const string input6[]);
int calculateNoOfWaitingDays(const string input7Str, const string input7Matrix, const int N7);

////////////////////////////////////////////////////////////////////////////
/// STUDENT'S ANSWER HERE
////////////////////////////////////////////////////////////////////////////

std::vector<int> convertStringInt(std::string coverter[])
{
    std::vector<int> result;
    return result;
}
string readyForBattle(const string ID[], const int NID, const string input1[], const int N1)
{
    char Letters[4][7] = 
    {
        { 'E', 'F', 'G', 'H', 'I', 'J', 'K' },
        { 'L', 'M', 'N', 'O', 'P', 'Q', 'R' },
        { '#', 'T', 'U', 'V', 'W', 'X', 'Y' },
        { '@', 'A', 'S', 'Z', 'B', 'C', 'D' }
    };

    for (int i = 0; i != sizeof(input1) / sizeof(input1[0]); i++)
    {
        std::vector<char> converted = {};
        for (int j = 0; j != sizeof(input1[i]) / sizeof(string); j++)
        {
            int num = {};
            switch (input1[i][j])
            {
            case '1': { num += 1; break; }
            case '0': { num *= 2; break; }
            case ' ': {
                converted.push_back(num);
                num = 0;
                break; }
            }
        }

        /*for (const auto& i : converted)
        {
            if (i )
        }*/
    }
    std::string result;
    return result;
}
int decode(const string A, const string B)
{
    int total = 0;
    std::string::size_type pos = 0;
    while ((pos = A.find(B, pos)) != std::string::npos)
    {
        ++total;
        pos += B.length();
    }
    return total;
}
string findRoute(const string ID[], const int NID, const string input3[])
{
    string result = {};
    return result;
}
string decodeVfunction(const string A, const string B)
{
    string result = {};
    return result;
}
string findBetrayals(const string input5[], const int N5)
{
    string result = {};
    return result;
}
int attack(const string input6[])
{
    int max[2] = { 10, 0 };
    for (int i = 0; i != 10; i++)
    {
        int soldier = 0;
        for (int j = 0; j != 10; j++)
        {
            if (input6[i][j] == '1') soldier++;
            if (input6[i][j] == '2')
            {
                soldier = 10;
                break;
            }
        }

        if (soldier < max[0])
        {
            max[0] = soldier;
            max[1] = i;
        }
    }
    return max[1];
}
int calculateNoOfWaitingDays(const string input7Str, const string input7Matrix, const int N7)
{
    std::vector<int, int> resultMatrix;
    for
    {

    }
    return resultMatrix[&input7Matrix[2]][&input7Matrix[3]] % input7Matrix[1];
}

#endif /* MONGOL_H */
