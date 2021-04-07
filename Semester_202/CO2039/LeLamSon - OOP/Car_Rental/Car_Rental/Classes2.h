#include <iostream>
#include <vector>
#include <regex>

using namespace std;
class Vehicle
{
protected:
    float cost;
    string type;
    string name;
public:
    Vehicle(float cost, const string& type, const string& name)
        :cost(cost), type(type), name(name)
    {

    };
    string GetName()const
    {
        return name;
    }
    string GetType()const
    {
        return type;
    }
    float GetPrice()const
    {
        return cost;
    }
    virtual void CanRun() = 0;
};
class Car : public Vehicle
{
public:
    Car(float cost, const string& type, const string& name)
        :Vehicle(cost, type, name)
    {

    }
    void CanRun()
    {
        cout << "Car run with 4 wheels\n";
    }
};

class Driver
{
private:
    string name;
    int age;
    string email;
    string address;
public:
    Driver(string name, int age, string email, string address)
        :name(name), age(age), email(email), address(address)
    {
    };
    void SetName(const string& iname)
    {
        name = iname;
    }
    string GetName()const
    {
        return name;
    }
    void SetName(string& iemail)
    {
        email = iemail;
    }
    string GetEmail()const
    {
        return email;
    }
    void SetAddress(const string& iaddress)
    {
        address = iaddress;
    }
    string GetAddress()const
    {
        return address;
    }
};
class Garage
{
private:
    vector<Car> fleet;
    string location;
    int Size;
public:
    Garage(string& location)
        :location(location) {};
    int GetSize()const
    {
        return fleet.size();
    }
    string GetLocation()const
    {
        return location;
    }
    void AddCar(Car tempt)
    {
        fleet.push_back(tempt);
    }
    void RemoveCar(Car tempt)
    {
        for (int i = 0; i < fleet.size(); i++)
        {
            if (fleet[i].GetName() == tempt.GetName())
            {
                cout << "Car exist\n";
                return;
            }
            else cout << "Car not exist\n";
        }
    }
};
class RentalContract
{
private:
    Driver d;
    string time;
    string date;
    float payment;
    Garage g;
    //vector<Garage> GarageAroundTheWorld;
public:
    RentalContract(Driver d, string time, string date, float payment, Garage g)
        :d(d), time(time), date(date), payment(payment), g(g)
    {
    }
    void SignContract(const string& location, const string& Vehicle)
    {
        if (location == Garage.GetLocation())
        {

        }
    }
};

int main()
{
    Vehicle* v = new Car(100, "Aventador", "Lambo");
    v->CanRun();
    delete v;
    return 0;
}
