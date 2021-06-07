#pragma once

#include <string>
#include <vector>
#include <iostream>
using namespace std;

class Student : public Person
{
private: 
	struct DOB
	{
		int day;
		int month;
		int year;
	};
	string name;
public:
	Student(DOB date, string name) : DOB(date), name(name)
	{
		std::cout << "New student created!\n Name:" << name <<
			"\nDOB:" << DOB.day << "/" << DOB.month << "/" << DOB.year << '\n';
	}
	~Student();
	{
		std::cout << "Deleted student ID:" << ID << '\n';
	}
};
class Class : public Student
{
};

//abstract class
class Person
{
private:
	int ID;
public:
	Person(int ID) : ID(ID) {}
	virtual ~Person() { std::cout << "Destruction of person id:" << ID << '\n'; }
};