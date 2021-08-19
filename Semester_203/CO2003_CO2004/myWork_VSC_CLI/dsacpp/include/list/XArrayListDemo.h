/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   XArrayListDemo.h
 * Author: LTSACH
 *
 * Created on 19 August 2020, 21:05
 */

#ifndef XARRAYLISTDEMO_H
#define XARRAYLISTDEMO_H
#include <chrono>
#include <iostream>
#include <iomanip>
#include "list/XArrayList.h"
#include "util/Point.h"
#include "util/ArrayLib.h"
using namespace std;

void xlistDemo1(){
    XArrayList<int> iList;
    for(int i = 0; i< 10 ; i++)
        iList.add(i, i*i);
    
    //iList.dump();
    for(XArrayList<int>::Iterator it=iList.begin(); it != iList.end(); it++ )
        cout << *it << ", found at: " << iList.indexOf(*it) << endl;
    cout << endl;
    int item = 120;
    int foundIdx = iList.indexOf(item);
    cout    << "lookup for " << item  << " found at: " << foundIdx << endl;
}

void xlistDemo2(){
    XArrayList<Point> alist;
    alist.add(Point(23.2f, 25.4f));
    alist.add(Point(24.6f, 23.1f));  
    alist.println();
}

void xlistDemo3(){
    XArrayList<Point> alist;
    alist.add(Point(23.2f, 25.4f));
    alist.add(Point(24.6f, 23.1f));  
    
    int idx1 = alist.indexOf(Point(24.6f, 23.1f));
    int idx2 = alist.indexOf(Point(24.61f, 23.1f));
    
    cout << "result 1 : " << idx1 << endl;
    cout << "result 2 : " << idx2 << endl;
}

void xlistDemo4(){
    XArrayList<Point*> list1(&XArrayList<Point*>::free, &Point::pointEQ);
    list1.add(new Point(23.2f, 25.4f));
    list1.add(new Point(24.6f, 23.1f));  
    list1.add(new Point(12.5f, 22.3f)); 
    
    for(XArrayList<Point*>::Iterator it = list1.begin(); it != list1.end(); it++)
        cout << **it << endl;
    
    Point* p1 = new Point(24.6f, 23.1f); //should be found in list
    Point* p2 = new Point(124.6f, 23.1f); //should not be found
    cout << *p1 << "=> " << (list1.contains(p1)? "found; " : "not found; ")
                << " indexOf returns: " << list1.indexOf(p1) << endl;
    cout << *p2 << "=> " << (list1.contains(p2)? "found; " : "not found; ")
                << " indexOf returns: " << list1.indexOf(p2) << endl;
    
    ///Different results if not pass &Point::equals
    cout << endl << endl;
    XArrayList<Point*> list2(&XArrayList<Point*>::free);
    list2.add(new Point(23.2f, 25.4f));
    list2.add(new Point(24.6f, 23.1f));  
    list2.add(new Point(12.5f, 22.3f)); 
    
    for(XArrayList<Point*>::Iterator it = list2.begin(); it != list2.end(); it++)
        cout << **it << endl;
    
    cout << *p1 << "=> " << (list2.contains(p1)? "found; " : "not found; ")
                << " indexOf returns: " << list2.indexOf(p1) << endl;
    cout << *p2 << "=> " << (list2.contains(p2)? "found; " : "not found; ")
                << " indexOf returns: " << list2.indexOf(p2) << endl;
    
    delete p1; delete p2;
}

void xlistDemo5(){
    XArrayList<int> arr;
    arr.add(0,1);
    arr.add(0,2);
    arr.add(0,3);
    arr.add(0,4);
    arr.add(0,5);
    arr.add(0,6);
    arr.add(0,7);
    arr.add(0,8);
    arr.add(0,9);
    arr.add(0,10);
    arr.add(0,11);
    arr.println();
}

void print(long double arr[], int size, int n, int progress)
{
    cout  << fixed << setw(2) << setprecision(7)
          << "[" << progress << "/100]:" << '\t'
          << (int)(arr[0]/n) << "\t -> \t";
    arr[0] = 0;
    for (int i = 1; i < size; i++)
    {
          cout  << arr[i]/n;
          if (i == size-1) cout << endl;
          else cout << ",\t";
          arr[i] = 0;
    }
}

template<class T>
T* search(IList<T>* &list, T key)
{ 
    if (list->indexOf(key) == -1)   return NULL;
    T* result = &(list->get(list->indexOf(key)));
    return result;
}

long double searchList(IList<int>* &list, int nexec, int ntries)
{
    int* intArray = genIntArray(nexec*ntries, 1, (int)(list->size()) - 1);
    srand(time(0));
    long double total = 0;
    for (auto size = 0; size < nexec * ntries; size++)
    {
        auto start = chrono::high_resolution_clock::now();
        int* result = search(list, intArray[size]);
        auto end = chrono::high_resolution_clock::now();
        long double duration = chrono::duration_cast<chrono::milliseconds>(end - start).count();
        total += duration;
    }
    delete[] intArray;
    return total / (nexec * ntries);
}

long double addIndex(IList<int>* &list, int nexec, int ntries)
{
    srand(time(0));
    long double total = 0;
    for (int size = 0; size < nexec * ntries; size++)
    {
        auto start = chrono::high_resolution_clock::now();
        list->add((int)(rand() % list->size()), (int)(rand() % 10000));
        auto end = chrono::high_resolution_clock::now();
        long double duration = chrono::duration_cast<chrono::milliseconds>(end - start).count();
        total += duration;
    }
    return total / (nexec * ntries);
}

void xlistDemo6()
{
    XArrayList<int> list;
    int nsizes = 100;
    int* ptr_sizes = genIntArray(nsizes, 1, 2000);
    long double result[3] = {};
    for (int i = 0; i < nsizes; i++)
    {
        for (int j = 0; j < ptr_sizes[i]; j++)
            list.add(j);
        result[0]               += ptr_sizes[i];
        long double addrand     = addIndex(&list, 10, 20);
        result[1]               += addrand;
        long double searchrand  = searchList(&list, 10, 20);
        result[2]               += searchrand;
        if (i%10 == 0 && i != 0) print(result, 3, 10, i);
        list.clear();
    }
    delete[] ptr_sizes;
}

#endif /* XARRAYLISTDEMO_H */

