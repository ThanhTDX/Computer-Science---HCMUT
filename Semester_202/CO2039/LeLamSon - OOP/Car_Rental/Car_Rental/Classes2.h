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
    Vehicle(float mcost, const string& mtype, const string& mname)
        :cost(cost), type(type), name(name)
    {
        cost = mcost;
        type = mtype;
        name = mname;
    };
    string GetName()
    {
        return name;
    }
    string GetType()
    {
        return type;
    }
    float GetPrice()
    {
        return cost;
    }
    virtual void CanRun() = 0;
};

class Car : public Vehicle
{
public:
    Car(float mcost, const string& mtype, const string& mname)
        :Vehicle(cost, type, name)
    {
        cost = mcost;
        type = mtype;
        name = mname;
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
    Driver()
    {
        name = " ";
        age = -1;
        email = " ";
        address = " ";
    }
    Driver(string mname, int mage, string memail, string maddress)  :   name(name), age(age), email(email), address(address)
    {
        Driver newDriver = new Driver();
        newDriver.name = mname;
        newDriver.age = mage;
        newDriver.email = memail;
        newDriver.address = maddress;
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
    ~Driver()
    {
        delete newDriver;
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
    ~RentalContract()
    {
    }
};

int main()
{
    Vehicle* v = new Car(100, "Aventador", "Lambo");
    v->CanRun();
    delete v;
    return 0;
}
