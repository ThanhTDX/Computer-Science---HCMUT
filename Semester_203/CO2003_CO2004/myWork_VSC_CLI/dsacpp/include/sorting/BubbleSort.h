/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   BubbleSort.h
 * Author: LTSACH
 *
 * Created on 23 August 2020, 17:16
 */

#ifndef BUBBLESORT_H
#define BUBBLESORT_H

#include "sorting/ISort.h"

template<class T>
class BubbleSort: public ISort<T>{
public:
    void sort(T array[], int size, int (*comparator)(T&,T&)){
        //YOUR CODE HERE
        for (int i = 0; i < size; i++){
            bool noSwap = true;
            for (int j = 0; j < size-i-1; j++){
                if (comparator){
                    if (comparator(array[j+1], array[j]) == -1) {
                        T temp = array[j];
                        array[j] = array[j+1];
                        array[j+1] = temp;
                        noSwap = false;
                    }
                }
                else {
                    if (array[j] > array[j+1]){
                        T temp = array[j];
                        array[j] = array[j+1];
                        array[j+1] = temp;
                        noSwap = false;
                    }
                }
            }
            if (noSwap) break;
        }
    }
};


#endif /* BUBBLESORT_H */

