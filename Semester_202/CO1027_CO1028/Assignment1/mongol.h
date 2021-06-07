//
// Created by Nhan Nguyen on 01/03/2021.
//
#ifndef MONGOL_H
#define MONGOL_H

// The library here is concretely set, students are not allowed to include any other libraries.

string readyForBattle(const string ID[], const int NID, const string input1[], const int N1);
int decode(const string A, const string B);                 
string findRoute(const string input3);                      
string decodeVfunction(const string A, const string B);
string findBetrayals(const string input5[], const int N5);
int attack(const string input6[]);                          
int calculateNoOfWaitingDays(const string input7Str, const string input7Matrix[], const int k);

////////////////////////////////////////////////////////////////////////////
/// STUDENT'S ANSWER HERE
////////////////////////////////////////////////////////////////////////////

std::vector<std::string> fromStringToVector(std::string sentence, std::string delim)
{
    std::vector<std::string> result;
    while (sentence.size())
    {
        int index = sentence.find(delim);
        if (sentence.find(delim) != std::string::npos)
        {
            result.push_back(sentence.substr(0, index));
            sentence = sentence.substr(index + delim.size());
            if (sentence.size() == 0)
                result.push_back(sentence);
        }
        else
        {
            result.push_back(sentence);
            sentence = "";
        }
    }
    return result;
}
string readyForBattle(const string ID[], const int NID, const string input1[], const int N1)
{
    char Letters[4][7] =
    {
        {'E', 'F', 'G', 'H', 'I', 'J', 'K'},
        {'L', 'M', 'N', 'O', 'P', 'Q', 'R'},
        {'#', 'T', 'U', 'V', 'W', 'X', 'Y'},
        {'@', 'A', 'S', 'Z', 'B', 'C', 'D'} };
    std::string result;
    bool king = false, general = false;
    for (int i = 0; i < NID; i++)
    {
        if ((int)ID[i].find("VUA") == 0)
            king = true;
        if (ID[i].find("THD") != std::string::npos &&
            (int)ID[i].find("THD") != 0 &&
            (int)ID[i].find("THD") != (int)ID[i].size() - 3)
            general = true;
    }

    for (int i = 0; i < N1; i++)
    {
        std::string LConvert, subWord;
        bool reverse = false, addLetter = false;
        std::vector<std::string> vector = fromStringToVector(input1[i], " ");
        //find word
        for (const auto& i : vector)
        {
            int row = 0, col = ((int)i.size() / 2 - 1) % 7;
            //only check first 2 letters, rests must be the same.

            if (i.substr(0, 2) == "00")
                row = 0;
            else if (i.substr(0, 2) == "01")
                row = 1;
            else if (i.substr(0, 2) == "10")
                row = 2;
            else if (i.substr(0, 2) == "11")
                row = 3;

            //incoming not-so-weird part
            //why reverse and addLetter? for # and @ - they can appear in same sentence
            //LConvert will hold only the result to then be converted in NID.

            if ((addLetter || reverse) && Letters[row][col] != '@' && Letters[row][col] != '#')
                subWord += Letters[row][col];

            //Check if letter = #
            //Add next alphabetical letter
            if (Letters[row][col] == '#' || (&i == &(vector.back()) && addLetter))
            {
                if (!addLetter)
                {
                    addLetter = true;
                    if (reverse)
                    {
                        subWord = string(subWord.rbegin(), subWord.rend());
                        LConvert += subWord;
                        subWord = "";
                        reverse = false;
                    }
                }
                else
                {
                    if (subWord.back() == 'Z')
                        subWord += "A";
                    else
                        subWord += subWord.back() + 1;
                    LConvert += subWord;
                    subWord = "";
                    if (Letters[row][col] == '#') addLetter = true;
                    else addLetter = false;
                }
            }
            //Check if letter = @
            // subword -> reverse
            else if (Letters[row][col] == '@' || (&i == &(vector.back()) && reverse))
            {
                if (!reverse)
                {
                    reverse = true;
                    if (addLetter)
                    {
                        if (subWord.back() == 'Z')
                            subWord += "A";
                        else
                            subWord += subWord.back() + 1;
                        LConvert += subWord;
                        subWord = "";
                        addLetter = false;
                    }
                }
                else
                {
                    subWord = string(subWord.rbegin(), subWord.rend());
                    LConvert += subWord;
                    subWord = "";
                    if (Letters[row][col] == '@') reverse = true;
                    else reverse = false;
                }
            }
            else if (!addLetter && !reverse)
                LConvert += Letters[row][col];
        }

        //if ID has VUA
        //1. create rConvert = reverse LConvert
        //2. compare index - = bigger word
        if (king)
        {
            std::string rConvert;
            for (int a = 0; a < (int)LConvert.size(); a++)
            {
                int b = (int)LConvert.size() - a;
                if ((int)LConvert.size() % 2 == 1)
                    b--;
                else if (a % 2 == 0)
                    b -= 2;
                rConvert += LConvert[b];
            }
            for (int k = 0; k < (int)LConvert.size(); k++)
            {
                LConvert[k] = (LConvert[k] > rConvert[k]) ? LConvert[k] : rConvert[k];
            }
        }
        //if BID has THD
        //1. erase index % 3 = 0
        //2. sort LConvert with small word first
        if (general)
        {
            for (int j = (int)LConvert.size() - 1; j >= 0; j--)
            {
                if (j % 3 == 0)
                    LConvert.erase(LConvert.begin() + j);
            }
            for (int k = 0; k < (int)LConvert.size() - 1; k++)
            {
                int small = k;
                for (int l = k + 1; l < (int)LConvert.size(); l++)
                {
                    if (LConvert[small] > LConvert[l])
                        small = l;
                }
                char temp = LConvert[small];
                LConvert[small] = LConvert[k];
                LConvert[k] = temp;
            }
        }
        result += LConvert;
        if (i != N1 - 1)
            result += ' ';
    }
    return result;
}
int decode(const string A, const string B)
{
    int count = 0;
    std::string subA = A;
    while ((int)subA.size() != 0 || (int)subA.size() < (int)B.size())
    {
        int index = subA.find(B);
        if (subA.find(B) != std::string::npos)
        {
            subA = subA.substr(index + 1);
            count++;
        }
        else break;
    }
    return count;
}
string findRoute(const string input3)
{
    //12 9 ULDULLD
    //U->D->L->R - 0->1->2->3
    std::vector<std::string> vectorinput3 = fromStringToVector(input3, " ");
    int N = stoi(vectorinput3[0]);
    int B = stoi(vectorinput3[1]);
    std::string S = vectorinput3[2];
    int size = S.size();
    int x = 0, y = 0;

    B = B % size; if (B < 0) B += size;
    S = S.substr(size - B, size) + S.substr(0, size - B);

    for (int i = 0; i < (int)S.size(); i++)
    {
        int numConvert = abs(N - 2 * i);
        switch (S[i])
        {
        case 'U':   break;
        case 'D':   numConvert += 1;    break;
        case 'L':   numConvert += 2;    break;
        case 'R':   numConvert += 3;    break;
        }
        switch (numConvert % 4)
        {
        case 0:     y++;    break;
        case 1:     y--;    break;
        case 2:     x--;    break;
        case 3:     x++;    break;
        }
    }
    return "(" + to_string(x) + "," + to_string(y) + ")";
}
string decodeVfunction(const string A, const string B)
{
    int a = (int)(A.size() / 3) * (int)(B.size() / 3);
    std::string result = "";
    for (int i = a; i != 0; i--) result += "V(";
    result += "0";
    for (int i = a; i != 0; i--) result += ")";
    return result;
}
string findBetrayals(const string input5[], const int N5)
{
    struct  Suspect
    {
        char    word;
        int     count;
    };
    std::string result;
    std::vector<Suspect> vec;
    for (int i = 0; i < N5; i++)
    {
        std::string word = input5[i];
        for (int j = 0; j < (int)word.size(); j++)
        {
            bool newSuspect = true;
            for (auto& i : vec)
            {
                if (i.word == word[j])
                {
                    i.count += 6 - j;
                    newSuspect = false;
                    break;
                }
            }
            if (newSuspect)
            {
                Suspect name = { word[j], 6 - j };
                vec.push_back(name);
            }
        }
    }
    for (int i = 0; i < (int)vec.size(); i++)
    {
        for (int j = 0; j < (int)vec.size() - i - 1; j++)
        {
            if (vec[j].count < vec[j + 1].count ||
                (vec[j].count == vec[j + 1].count && vec[j].word > vec[j + 1].word))
            {
                auto temp = vec[j];
                vec[j] = vec[j + 1];
                vec[j + 1] = temp;
            }
        }
    }
    for (int i = 0; i < 3; i++)
    {
        result += vec[i].word;
    }
    return result;
}
int attack(const string input6[])
{
    int ans[2] = { 10, -1 };
    for (int i = 9; i != -1; i--)
    {
        int soldier = 0;
        std::string word = input6[i];
        for (int j = 0; j != 10; j++)
        {
            if (word[j] == '1')    soldier++;
            if (word[j] == '2')
            {
                soldier += 10;
                break;
            }
        }
        if (soldier < ans[0])
        {
            ans[0] = soldier;
            ans[1] = i;
        }
    }
    return ans[1];
}
int calculateNoOfWaitingDays(const string input7Str, const string input7Matrix[], const int k)
{
    std::vector<std::string> input7Vec = fromStringToVector(input7Str, " ");
    int N7 = stoi(input7Vec[0]);
    int V = stoi(input7Vec[1]);
    int i = stoi(input7Vec[2]);
    int j = stoi(input7Vec[3]);

    std::vector<std::string> initMatrix = fromStringToVector(input7Matrix[0], " ");

    long long int* result = new long long int[N7];
    long long int* tmp = new long long int[N7];
    for (int a = 0; a < N7; a++)
    {
        result[a] = stoi(initMatrix[i * N7 + a]);
        tmp[a] = 0;
    }
    for (int b = 1; b < k; b++)
    {
        std::vector<std::string> lineMat = fromStringToVector(input7Matrix[b], " ");
        for (int m = 0; m < N7; m++)
        {
            for (int n = 0; n < N7; n++)
            {
                tmp[n] += stoi(lineMat[m * N7 + n]) * result[m];
            }
        }
        for (int a = 0; a < N7; a++)
        {
            result[a] = tmp[a];
            tmp[a] = 0;
        }
    }
    int num = result[j] % V;
    delete[] result;
    delete[] tmp;
    return (num >= 0 ? num : V + num);
}
#endif /* MONGOL_H */
