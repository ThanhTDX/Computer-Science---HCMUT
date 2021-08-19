/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   SLinkedListDemo.h
 * Author: LTSACH
 *
 * Created on 19 August 2020, 21:16
 */

#ifndef SLINKEDLISTDEMO_H
#define SLINKEDLISTDEMO_H

#include <iostream>
#include <iomanip>
#include "SLinkedList.h"
#include "util/Point.h"
#include "util/sampleFunc.h"
using namespace std;

void slistDemo1(){
    SLinkedList<int> slist;
    for(int i = 0; i< 20 ; i++)
        slist.add(i*i);
    slist.println();
}
void slistDemo2(){
    SLinkedList<Point*> list1(&SLinkedList<Point*>::free, &Point::pointEQ);
    list1.add(new Point(23.2f, 25.4f));
    list1.add(new Point(24.6f, 23.1f));  
    list1.add(new Point(12.5f, 22.3f)); 
    
    for(SLinkedList<Point*>::Iterator it = list1.begin(); it != list1.end(); it++)
        cout << **it << endl;
    
    Point* p1 = new Point(24.6f, 23.1f); //found in list
    Point* p2 = new Point(124.6f, 23.1f); //not found
    cout << *p1 << "=> " << (list1.contains(p1)? "found; " : "not found; ")
                << " indexOf returns: " << list1.indexOf(p1) << endl;
    cout << *p2 << "=> " << (list1.contains(p2)? "found; " : "not found; ")
                << " indexOf returns: " << list1.indexOf(p2) << endl;
    
    ///Different results if not pass &Point::equals
    cout << endl << endl;
    SLinkedList<Point*> list2(&SLinkedList<Point*>::free);
    list2.add(new Point(23.2f, 25.4f));
    list2.add(new Point(24.6f, 23.1f));  
    list2.add(new Point(12.5f, 22.3f)); 
    
    for(SLinkedList<Point*>::Iterator it = list2.begin(); it != list2.end(); it++)
        cout << **it << endl;
    
    cout << *p1 << "=> " << (list2.contains(p1)? "found; " : "not found; ")
                << " indexOf returns: " << list2.indexOf(p1) << endl;
    cout << *p2 << "=> " << (list2.contains(p2)? "found; " : "not found; ")
                << " indexOf returns: " << list2.indexOf(p2) << endl;
    delete p1; delete p2;
}

void slistDemo3()
{
    std::cout << "SLinkedList<int>[3]: add/removeX/indexOf/contains";
    SLinkedList<int> list;
    std::cout << "List size:" << list.size() << '\n';
    int values[]   = {10,  15,  2,   6,  4,  7,   40,  8};
    for(int idx=0; idx < 8; idx++) list.add(values[idx]);
    list.println();
    std::cout << '\n';
    list.removeItem(8);
    list.println();
    std::cout << '\n';
    list.add(100);
    list.println();
    std::cout << '\n';
}

void slistDemo4()
{
    SLinkedList<int> list;
    list.add(4);
    list.println();
    list.add(6);
    list.println();
    std::cout << list.removeItem(19) << endl;
    std::cout << list.get(0) << endl;
    std::cout << list.removeAt(0) << endl;
    list.println();
}

void slistDemo5()
{
    SLinkedList<Point> list; 
    Point* sampletest = Point::genPoints(5, 0, 1);
    for (int i = 0; i < 5; i++)
    {
        list.add(sampletest[i]);
    }
    list.println(Point::point2str);
    Point *random = new Point(23.2f, 25.4f);
    Point another{32.5, 22.8};
    // float val = *random;
    // std::cout << "\n" << val << " " << (float)(*random) << endl;
    std::cout << (float)(another) << endl;
}

void slistDemo6()
{

}
#endif /* SLINKEDLISTDEMO_H */

