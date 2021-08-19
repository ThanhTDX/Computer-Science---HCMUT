/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   ListSort.h
 * Author: LTSACH
 *
 * Created on 12 September 2020, 09:56
 */

#ifndef LISTSORT_H
#define LISTSORT_H

#include "sorting/DLinkedListSE.h"
#include "sorting/SLinkedListSE.h"
#include "sorting/XArrayListSE.h"
#include "util/Point.h"
#include "util/ArrayLib.h"
#include "geom/Point3D.h"

int sortIntComparator(int& lhs, int& rhs){
    if(lhs < rhs) return +1;
    else if(lhs > rhs) return -1;
    else return 0;
}
void listSortDemo1(){
    int items[] = {18, 5, 12, 7, 89, 1, 3, 24};
    DLinkedListSE<int> list;
    for(int i=0; i < 8; i++) list.add(items[i]);
    list.println();
    list.sort();
    list.println();
    list.sort(&sortIntComparator);
    list.println();
}

int sortPointComparator(Point3D*& lhs, Point3D*& rhs){
    if(lhs->radius() < rhs->radius()) return -1;
    else if(lhs->radius() > rhs->radius()) return +1;
    else return 0;
}

int sortPointComparatorDESC_Y(Point3D*& lhs, Point3D*& rhs){
    if(lhs->radius() < rhs->radius()) return +1;
    else if(lhs->radius() > rhs->radius()) return -1;
    else return 0;
}

void listSortDemo2(){
    int size = 20;
    Point3D* items = Point3D::genPoints(size, -10, 10);
    DLinkedListSE<Point3D*> list;
    for(int i=0; i < size; i++) list.add(&items[i]);
    
    list.println(&Point3D::toString);
    
    cout << "Ascending:" << endl;
    list.sort(&sortPointComparator);
    list.println(&Point3D::toString);
    
    cout << "Descending:" << endl;
    list.sort(&sortPointComparatorDESC_Y);
    list.println(&Point3D::toString);
 
    //
    delete []items;
}

void listSortDemo3(){
    int size = 20;
    Point3D* items = Point3D::genPoints(size, -10, 10);
    XArrayListSE<Point3D*> list;
    for(int i=0; i < size; i++) list.add(&items[i]);
    
    list.println(&Point3D::toString);
    
    cout << "Ascending:" << endl;
    list.sort(&sortPointComparator);
    list.println(&Point3D::toString);
    
    cout << "Descending:" << endl;
    list.sort(&sortPointComparatorDESC_Y);
    list.println(&Point3D::toString);
 
    //
    delete []items;
}

void listSortDemo4(){
    int size = 20;
    Point3D* items = Point3D::genPoints(size, -10, 10);
    SLinkedListSE<Point3D*> list;
    for(int i=0; i < size; i++) list.add(&items[i]);
    
    list.println(&Point3D::toString);
    
    cout << "Ascending:" << endl;
    list.sort(&sortPointComparator);
    list.println(&Point3D::toString);
    
    cout << "Descending:" << endl;
    list.sort(&sortPointComparatorDESC_Y);
    list.println(&Point3D::toString);
 
    //
    delete []items;
}


bool isOrdered(DLinkedListSE<int>& list, bool ascending=true){
    bool ordered = true;
    DLinkedListSE<int>::Iterator it = list.begin();
    int prev = *it;
    it++;
    for(; it != list.end(); it++){
        int cur = *it;
        if(ascending){
            //is ascending?
            if(cur < prev){
                ordered = false;
                break;
            }
            else prev = cur;
        }
        else{
            //is descending?
            if(cur > prev){
                ordered = false;
                break;
            }
            else prev = cur;
        }
    }
    return ordered;
}

bool isOrderedBWD(DLinkedListSE<int>& list, bool ascending=true){
    bool ordered = true;
    DLinkedListSE<int>::BWDIterator it = list.bbegin();
    int next = *it;
    it--;
    for(; it != list.bend(); it--){
        int cur = *it;
        if(ascending){
            //is ascending?
            if(cur > next){
                ordered = false;
                break;
            }
            else next = cur;
        }
        else{
            //is descending?
            if(cur < next){
                ordered = false;
                break;
            }
            else next = cur;
        }
    }
    return ordered;
}

void listSortDemo5(){
    for(int size = 1; size < 200; size++){
    int* items = genIntArray(size, -20, 20);
    DLinkedListSE<int> list;
    for(int i=0; i < size; i++) list.add(items[i]);
    
    list.println();
    
    cout << "Ascending:" << endl;
    list.sort();
    list.println();
    if(!isOrdered(list, true)) break;

    cout << "Descending:" << endl;
    list.sort(&sortIntComparator);
    list.println();
    if(!isOrderedBWD(list, true)) break;
 
    //
    delete []items;
    }
}

#endif /* LISTSORT_H */

