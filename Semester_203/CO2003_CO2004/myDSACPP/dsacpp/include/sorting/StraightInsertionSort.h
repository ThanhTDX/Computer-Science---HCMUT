/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   StraightInsertionSort.h
 * Author: LTSACH
 *
 * Created on 23 August 2020, 16:24
 */

#ifndef STRAIGHTINSERTIONSORT_H
#define STRAIGHTINSERTIONSORT_H
#include "sorting/ISort.h"

template<class T>
class StraightInsertionSort: public ISort<T>{
public:
    void sort(T array[], int size, int (*comparator)(T&,T&)){
        //YOUR CODE HERE
        int count = 1;
        while (count != size)
        {
            int cur = count;
            while (cur != 0)
            {
                if (comparator){
                    if (comparator(array[cur], array[cur-1]) == -1)
                    {
                        T temp = array[cur];
                        array[cur]= array[cur-1];
                        array[cur-1] = temp;
                        cur--;
                    }
                    else break;
                }
                else {
                    if (array[cur] < array[cur-1])
                    {
                        T temp = array[cur];
                        array[cur] = array[cur-1];
                        array[cur-1] = temp;
                        cur--;
                    }
                    else break;
                }
            }
            count++;
        }
    }
};

#endif /* STRAIGHTINSERTIONSORT_H */

