#include "student_info.h"

int main()
{
    int choice;
    std::vector<student_info> list;

    do
    {
        std::cout << "Choose an option:\n"
        "1. Create new student.\n"
        "2. Display all students.\n"
        "3. Delete a name.\n"
        "4. Exit the program.";
        std::cin >> choice;
    switch (choice)
    {
        case 1:
            {
                std::string name;
                std::cin >> name;
                student_info::student_info(name);
                std::pushback
            }
        case 2:
            {
                displayList(std::vector<student_info> list);
            }
        case 3:
            {

            }
        case 4:
            {
                std::cout << "Exited.";
                return 0;
            }
    }
    } while (choice);
    return 0;
}
