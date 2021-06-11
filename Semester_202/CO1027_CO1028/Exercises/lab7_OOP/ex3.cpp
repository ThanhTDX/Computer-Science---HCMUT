/*In function main(), write program to create an array of objects belong to class Course with n elements (n is inputted by user using dynamic array and new).
 Then input and display the data for n objects using the implemented functions getinfo() and disinfo().*/

#include<iostream>

using namespace std;

class Course {
    private:
        int ID;
        int numOfStudent;
        int numOfTeacher;
        int numOfTA;
    public:
        void getinfo();
        void disinfo();
};

void Course::getinfo() {
   cout << "ID: ";
   cin >> ID;
   cout << "Number of Students: ";
   cin >> numOfStudent;
   cout << "Number of Teachers: ";
   cin >> numOfTeacher;
   cout << "Number of TAs: ";
   cin >> numOfTA;
}

void Course::disinfo()
{
   cout<<endl;
   cout<< "CourseID = "<< ID << endl;
   cout<< "Number of student = " << numOfStudent << endl;
   cout<< "Number of teacher = " << numOfTeacher << endl;
   cout<< "Number of TA = " << numOfTA<< endl;
}


int main() {
    int n;
    std::cin >> n;
    if (n <= 0) return 0;
    Course courses[n];
    for (int i = 0; i < n; i++)
        courses[i].getinfo();
    for (int i = 0; i < n; i++)
        courses[i].disinfo();    
}