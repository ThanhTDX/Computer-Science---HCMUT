/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   Point3D.cpp
 * Author: LTSACH
 * 
 * Created on 8 June 2021, 18:42
 */

#include "geom/Pair.h"

template<class A, class B>
ostream &operator<<( ostream &os, const Pair<A,B>& pair){
    os << "P(" << fixed 
            << setw(6) << setprecision(2) << pair.key << "," 
            << setw(6) << setprecision(2) << pair.value
       << ")";
    return os;
}

template<class A, class B>
Pair<A,B>::Pair(A key, B value) {
    this->key = key;
    this->value = value;
}

template<class A, class B>
Pair<A,B>::Pair(const Pair& pair) {
    this->key = pair.key;
    this->value = pair.value;
}

template<class A, class B>
Pair<A,B>::~Pair() {
}

template<class A, class B>
void Pair<A,B>::setX(A x){
    this->key = x;
}

template<class A, class B>
A Pair<A,B>::getX() const{
    return this->key;
}

template<class A, class B>
void Pair<A,B>::setY(B y){
    this->value = y;
}

template<class A, class B>
B Pair<A,B>::getY() const{
    return this->value;
}

template<class A, class B>
bool Pair<A,B>::operator==(Pair<A,B> rhs){
    return  (abs(this->key - rhs.key) < EPSILON) &&
            (abs(this->value - rhs.value) < EPSILON);
}

template<class A, class B>
Pair<A,B> Pair<A,B>::operator+(Pair<A,B> dir){
    return Pair(this->key + dir.getX(), this->value + dir.getY());
}

template<class A, class B>
void Pair<A,B>::println(){
    cout << *this << endl;
}

template<class A, class B>
bool Pair<A,B>::equals(Pair& lhs, Pair& rhs){
    return  lhs == rhs;
}
template<class A, class B>
bool Pair<A,B>::equals(Pair*& lhs, Pair*& rhs){
    return  *lhs == *rhs;
}

template<class A, class B>
string Pair<A,B>::toString(Pair& point){
    stringstream os;
    os  << point;
    return os.str();
}

template<class A, class B>
string Pair<A,B>::toString(Pair*& point){
    return toString(*point);
}

template<class A, class B>
Pair<A,B>* Pair<A,B>::genPairs(int size, float minValue, float maxValue, 
                            bool manualSeed, int seedValue){
    Pair<A,B>* head = new Pair<A,B>[size];
        
    std::default_random_engine* engine;
    if(manualSeed)
        engine = new std::default_random_engine(static_cast<long unsigned int>(seedValue));
    else
        engine = new std::default_random_engine(static_cast<long unsigned int>(time(0)));
    uniform_real_distribution<double> dist(minValue, maxValue);

    //
    for(int idx=0; idx < size; idx++){
        A key = dist(*engine);
        B value = dist(*engine);
        head[idx] = Pair(key, value);
    }
    delete engine;
    return head;
}

template<class A, class B>
void Pair<A,B>::println(Pair<A,B>* head, int size){
    stringstream os;
    os << "[\n";
    for(int idx=0; idx < size; idx++) os << head[idx] << endl;
    os << "]\n";
    cout << os.str() << endl;
    return;
}

