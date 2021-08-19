/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   PAIR.h
 * Author: LTSACH
 *
 * Created on 8 June 2021, 18:42
 */

#ifndef PAIR_H
#define PAIR_H

#include <iostream>
#include <iomanip>
#include <math.h>
#include <random>
#include <sstream>
using namespace std;

#define EPSILON (1E-8)

template <class A, class B>
class Pair{
public:
    template <class C, class D>
    friend ostream &operator<<( ostream &os, const Pair<C,D>& pair);
    
    Pair(A key=0, B value=0);
    Pair(const Pair& pair);
    virtual ~Pair();
    
    //Setter and Getter
    void setX(A z);
    A getX() const;
    void setY(B z);
    B getY() const;
    
    //
    bool operator==(Pair rhs);
    Pair operator+(Pair dir);

    void println();
    
    //static section  
    static bool equals(Pair& lhs, Pair& rhs); //with pointer to point
    static bool equals(Pair*& lhs, Pair*& rhs); //with pointer to point
    static string toString(Pair& point);
    static string toString(Pair*& point);
    
    
    // The the two following: generate and print an array of Point3D
    static Pair* genPairs(  int size, 
                                float minValue=0, float maxValue=1, 
                                bool manualSeed=false, int seedValue=0);
    static void println(Pair* head, int size);
    
    
private:
    A key;
    B value;
};

#endif /* POINT3D_H */

