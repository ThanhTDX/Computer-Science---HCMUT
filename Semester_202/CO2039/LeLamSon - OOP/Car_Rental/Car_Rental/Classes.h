#pragma once
#ifndef CLASSES_H
#define CLASSES_H


class BookAndRent
{
	virtual void bookACar();
	virtual void SignAContract();
};

class Contract : public BookAndRent
{
private:
	Customer guest;
	Car item;

public:
	void bookACar();
	Contract()
	{
		guest = new Guest();
		item = new Car();
	}
	Contract(Customer newGuest);
	Contract(Car newItem);
	Contract(Customer newGuest, Car newItem);

	~Contract()
	{
		delete guest;
	}
};


class Customer
{
private:
	int age;
	std::string name;
	std::string address;
	std::string license;
	int DOB;
public:
	Customer()
	{
		age = -1;
		name = ' ';
		address = ' ';
	}
	Customer(int age, std::string name, std::string address, std::string)
	{

		this->age = age;
		this->name = name;
	}

	~Customer();
};

class Vehicle
{
private:
protected:
public:
	Vehicle();
	Vehicle(Attributes newCar);

	~Car();
};

class Condition
{
private:
public:
	Condition();
	Condition(details information);

	~Condition();
};
#endif CLASSES_H