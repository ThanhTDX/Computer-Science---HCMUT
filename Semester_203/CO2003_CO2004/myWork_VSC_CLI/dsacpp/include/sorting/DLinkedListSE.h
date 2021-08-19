/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   DLinkedListSE.h
 * Author: LTSACH
 *
 * Created on 31 August 2020, 14:13
 */

#ifndef DLINKEDLISTSE_H
#define DLINKEDLISTSE_H
#include "list/DLinkedList.h"
#include "sorting/ISort.h"

template<class T>
class DLinkedListSE: public DLinkedList<T>{
public:
    
    DLinkedListSE(
            void (*removeData)(DLinkedList<T>*)=0, 
            bool (*itemEQ)(T&, T&)=0 ) : 
            DLinkedList<T>(removeData, itemEQ){
    };
    void sort(int (*comparator)(T&,T&)=0){
        //YOUR CODE HERE

        //ISOLATE THE TAIL
        this->tail->prev->next = NULL;
        this->tail->prev = NULL;

        //SORT
        typename DLinkedList<T>::Node* first = this->head->next;
        first->prev = NULL;
        mergeSort(first, comparator);

        //REATTACH THE TAIL
        typename DLinkedList<T>::Node* last = this->head;
        while (last->next != NULL) last = last->next;

        last->next = this->tail;
        this->tail->prev = last;

        //REATTACH THE HEAD
        this->head->next = first;
        this->head->next->prev = this->head;
        //
    };
    
protected:
    static int compare(T& lhs, T& rhs, int (*comparator)(T&,T&)=0){
        if(comparator != 0) return comparator(lhs, rhs);
        else{
            if(lhs < rhs) return -1;
            else if(lhs > rhs) return +1;
            else return 0;
        }
    }
    void mergeSort(typename DLinkedList<T>::Node*& head, int (*comparator)(T&,T&)=0){
        //YOUR CODE HERE
        if (head != NULL && head->next != NULL)
        {
            typename DLinkedList<T>::Node* second;
            devide(head, second);
            mergeSort(head, comparator);
            mergeSort(second, comparator);
            merge(head, second, comparator);
        }
    };
    void devide(typename DLinkedList<T>::Node*& first, typename DLinkedList<T>::Node*& second){
        //YOUR CODE HERE
        typename DLinkedList<T>::Node* midpt = first;
        typename DLinkedList<T>::Node* endpt = first->next;
        while (endpt->next != NULL && endpt->next->next != NULL)
        {
            midpt = midpt->next;
            endpt = endpt->next->next;
        }
        second = midpt->next;
        midpt->next = NULL;
        second->prev = NULL;
    }
    void merge(typename DLinkedList<T>::Node*& first, typename DLinkedList<T>::Node*& second, int (*comparator)(T&,T&)=0){
        //YOUR CODE HERE
        // THIS IS DUMMY NODE
        typename DLinkedList<T>::Node* result = new typename DLinkedList<T>::Node::Node();
        // THIS IS ITERATOR
        typename DLinkedList<T>::Node* ptr = result;
        while (first != NULL && second != NULL)
        {
            //FIRST DATA INSERTED
            if (compare(first->data, second->data, comparator) == -1)
            {
                ptr->next = first;
                ptr->next->prev = ptr;
                first = first->next;
                ptr = ptr->next;
            }
            //SECOND DATA INSERTED
            else
            {
                ptr->next = second;
                ptr->next->prev = ptr;
                second = second->next;
                ptr = ptr->next;
            }
        }
        if (!first) 
        {
            ptr->next = second;
            ptr->next->prev = ptr;
        }
        else        
        {
            ptr->next = first;
            ptr->next->prev = ptr;
        }

        //RESULT = DUMMY NODE -> DELETE DUMMY NODE
        first = result->next;
        first->prev = NULL;
        result->next = NULL;
        delete result;
    }
};

#endif /* DLINKEDLISTSE_H */

