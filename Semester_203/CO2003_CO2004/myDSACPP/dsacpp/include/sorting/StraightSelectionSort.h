/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   StraightSelectionSort.h
 * Author: LTSACH
 *
 * Created on 23 August 2020, 17:10
 */

#ifndef STRAIGHTSELECTIONSORT_H
#define STRAIGHTSELECTIONSORT_H

#include "sorting/ISort.h"


template<class T>
class StraightSelectionSort: public ISort<T>{
public:   
    void sort(T array[], int size, int (*comparator)(T&,T&)){
        //YOUR CODE HERE
        int count = 0;
        while (count != size)
        {
            int idx = count;
            for (int i = count+1; i < size; i++)
            {
                if (comparator)
                {
                    if (comparator(array[idx], array[i]) == 1)
                        idx = i;
                }
                else {
                    if (array[idx] > array[i])
                        idx = i;
                }
            }
            T temp = array[count];
            array[count] = array[idx];
            array[idx] = temp;
            count++;
        }
    }
};



#endif /* STRAIGHTSELECTIONSORT_H */

