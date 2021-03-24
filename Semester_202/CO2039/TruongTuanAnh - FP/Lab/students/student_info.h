#pragma once
#ifndef STUDENT_INFO_H_INCLUDED
#define STUDENT_INFO_H_INCLUDED

#include <iostream>
#include <vector>
#include <string>


void displayList(const std::vector<std::string>& list)
{
    std::cout << "List of all students:\n";
    for (const auto &i : list)
    {
        std::cout << i << '\n';
    }
}

void deleteStudent(std::vector<std::string>& list, std::string dName)
{
    if (list.size() == 0)
    {
        std::cout << "There's no one to delete, return.\n";
        return;
    }
    int size = list.size();
    list.erase(std::remove(list.begin(), list.end(),dName), list.end());
    if (size == list.size()) std::cout << "There's no one with that name\n";
    else std::cout << "Done\n";
}
#endif // STUDENT_INFO_H_INCLUDED
