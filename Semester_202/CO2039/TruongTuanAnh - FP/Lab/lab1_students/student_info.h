#ifndef STUDENT_INFO_H_INCLUDED
#define STUDENT_INFO_H_INCLUDED

#include <iostream>
#include <vector>
#include <string>

class student_info
{
private:
    std::string name;

public:
    student_info()
    {
        name = '';
    }
    student_info(string newName)
    {
        name = newName;
    }
    ~student_info()
    {
        delete name;
    }
};


    student_info()
    {
        std::string newName;
        std::cout << "Enter new name:";
        getline(std::cin, newName);
        newStudent.name = newName;
    }
void displayList(const std::vector<student_info> &list)
{
    for (const auto &i: list)
    {
        std::cout << i << '\n';
    }
}

void deleteStudent
#endif // STUDENT_INFO_H_INCLUDED
