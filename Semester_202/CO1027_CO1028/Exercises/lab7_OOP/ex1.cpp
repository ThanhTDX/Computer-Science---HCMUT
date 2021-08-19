/*
Given the following class:

class Book {
public:
    Book(const char*);
    ~Book();
    void display();
private:
    char* name;
};

Implement constructor and destructor of Book so that the following program running without errors:
*/

#include<iostream>
#include<string.h>

using namespace std;

class Book {
    char* name;
public:
    Book(const char*);
    ~Book();
    void display();
    char* getName();
};

Book::Book(const char* newName) 
{
    name = new char[80];
    strcpy(name, newName);
}

Book::~Book()
{
    delete name;
}

void Book::display() {
    cout << "Book: " << name << endl;
}

char* Book::getName() {
    return name;
}

int main() {
    char *str, *checkDel;
    char* buf = new char[80];
    cin.get(buf, 79);
    str = new char[strlen(buf) + 1];
    checkDel = new char[strlen(buf) + 1];
    strcpy(str, buf);
    strcpy(checkDel, buf);
    delete buf;
    Book* newNovel =  new Book(str);
    delete str;
    newNovel->display();
    char* ptr = newNovel->getName();
    delete newNovel;
    for (unsigned int i = 0; i < strlen(checkDel); i++) {
        if (checkDel[i] != ptr[i]) {
            cout << "Deleted" << endl;
            return 0;
        }
    }
    cout << "Not deleted" << endl;
    return 0;
}