#pragma once
#ifndef CLASSES_H
#define CLASSES_H

class Contract
{
private:
	Customer guest;
	Car item;
	Condition rules;
public:
	Contract();
	Contract(Customer newGuest);
	Contract(Car newItem);
	Contract(Customer newGuest, Car newItem);

	~Contract();
};

class Customer
{
private:
	std::string name;
	int ID;
	long int phone;
public:
	Customer();
	Customer(std::string newName, int newID, long int newPhone);
	Customer(std::string newName);
	Customer(int newID);
	Customer(long int newPhone);

	~Customer();
};

class Car
{
private:
	int ID;
	std::string type;
protected:
	bool storage.isAvailable();
public:
	Car();
	Car(int newID, std::string newType);
	Car(int newID);
	Car(std::string newType);

	~Car();
};

class Condition
{
private:
	int borrowDate;
	int returnDate;
	std::string returnLocation;
public:
	Condition(int bDate, int rDate, std::string rLocation);
	Condition(int bDate, int rDate);
	Condition(std::string rLocation);

	~Condition();
};
#endif CLASSES_H