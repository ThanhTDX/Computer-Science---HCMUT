#include "student_info.h"

int main()
{
    int choice;
    std::vector<std::string> list;

    do
    {
        std::cout << "Choose an option:\n"
            "1. Create new student.\n"
            "2. Display all students.\n"
            "3. Delete a name.\n"
            "4. Exit the program.\n";
        while (!(std::cin >> choice)) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid input; please re-enter.\n";
        }
        switch (choice)
        {
            case 1:
            {
                std::string iname;
                std::cout << "Enter a new name:";
                std::cin.ignore();
                std::getline(std::cin, iname);
                std::string student{ iname };
                list.push_back(student);
                break;
            }
            case 2:
            {
                displayList(list);
                break;
            }
            case 3:
            {
                std::string dName;
                std::cout << "Choose a name to delete:\n";
                std::cin.ignore();
                std::getline(std::cin, dName);
                deleteStudent(list, dName);
                break;
            }
            case 4:
            {
                std::cout << "Exited.";
                return 0;
            }
            default:
            {
                std::cout << "ERROR\n";
            }
        }
    } while (choice);
    return 0;
}
