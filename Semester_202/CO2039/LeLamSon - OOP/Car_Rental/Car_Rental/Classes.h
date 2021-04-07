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
	enum Attributes
	{
		name,
		ID,
		phone,
	};
public:
	Customer();
	Customer(Attributes newCustomer);

	~Customer();
};

class Car
{
private:
	enum Attributes
	{
		ID,
		type,
	};
protected:
	bool storage.isAvailable();
public:
	Car();
	Car(Attributes newCar);

	~Car();
};

class Condition
{
private:
	enum details
	{
		borrowDate,
		returnDate,
		returnLocation,
	};
public:
	Condition();
	Condition(details information);

	~Condition();
};
#endif CLASSES_H