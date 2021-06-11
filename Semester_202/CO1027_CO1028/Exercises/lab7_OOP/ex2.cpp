/*Build class Coordinate included x and y (type float) are two coordinates in Oxy. 

Implement constructor receive two numbers x, y and assign to the x,y of the class respectively.
Implement functions  setX(), setY(), getX(), getY() for this class. Students choose the approriate returns.
Impletement function  distanceTo(Coordinate&) to calculate the Manhattan distance from a Coordinate to an input coordinate. (The Manhattan distance can be calculated as: d = abs(x1 – x2) + abs(y1 - y2))*/

#include <iostream>
#include <cmath>

using namespace std;

class Coordinate
{
private:
    float x;
    float y;
public:
    Coordinate() : x(0), y(0){};
    Coordinate(int x, int y) : x(x), y(y){};
    void setX(float x);
    void setY(float y);
    float getX();
    float getY();
    float distanceTo(Coordinate& point);
};

void Coordinate::setX(float x)
{
    this->x = x;
}

void Coordinate::setY(float y)
{
    this->y = y;
}

float Coordinate::getX()
{
    return this->x;
}

float Coordinate::getY()
{
    return this->y;
}

float Coordinate::distanceTo(Coordinate& point)
{
    return abs(this->x - point.x) + abs(this->y - point.y);
}
int main () {
    float Xa, Xb, Ya, Yb;
    cin >> Xa >> Xb >> Ya >> Yb;
    Coordinate a(1,2);
    Coordinate b(0,1);
    cout << a.distanceTo(b) << endl;
    a.setX(Xa); a.setY(Ya);
    b.setX(Xb); b.setY(Yb);
    cout << abs(a.getX() - b.getX()) + abs(a.getY() - b.getY()) << endl;
    cout << a.distanceTo(b) << endl;
    cout << abs(Xa - Xb) + abs(Ya - Yb);
    return 0;
}