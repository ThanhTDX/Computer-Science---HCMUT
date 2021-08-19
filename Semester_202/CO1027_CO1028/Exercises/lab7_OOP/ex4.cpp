/*Do the following requirements:

Build a class Integer included a private attribute val is an integer number. 
Implement the constructor: Integer(int).
Hiện thực constructor: Integer(Interger*).
Overloading operator + so that Integer(2) + Integer(3)  return Integer(5).
Overloading operator + so that Integer(3) + 2 return Integer(5).
Pay attention to the definition of function print() in the class and don't re-implement.*/

#include<iostream>
using namespace std;

class Integer
{
private:
    int val;
public:
    Integer() = default;
    Integer(int val);
    void print();
    Integer operator+(Integer num);
    Integer operator+(int num);
};

Integer::Integer(int val) : val(val) {};

Integer Integer::operator+(Integer num)
{
    return Integer(this->val + num.val);
}
Integer Integer::operator+(int num)
{
    return Integer(this->val + num);
}

void Integer::print() {
    cout << this->val << endl;
}

int main() {
    int x, y, z;
    cin >> x >> y >> z;
    Integer a(x);
    Integer b(y);
    Integer c(z);
    a.print(); b.print();
    (a + b + c + 4).print();
    return 0;
}