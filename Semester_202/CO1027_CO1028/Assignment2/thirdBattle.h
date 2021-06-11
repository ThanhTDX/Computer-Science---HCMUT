//
//  thirdBattle.h
//  KTLT ASS 3
//
//  Created by Nhân Nguyễn on 17/05/2021.
//
// Students can remove the final initial return of the functions

#ifndef thirdBattle_h
#define thirdBattle_h

#include "SLLDataController.h"
#include "ArrayDataController.h"
#include <vector>
#include <string>

//////////////////////////////////////////////////////
/// TASK 1
//////////////////////////////////////////////////////

bool push(Array& array, Soldier soldier){
    //Return true if push successfully, false otherwise
    //TODO
    return insertAt(array, soldier, array.size);
}

bool pop(Array& array){
    //Return true if pop successfully, false otherwise
    //TODO
    return removeAt(array, array.size - 1);
}

Soldier top(Array& array){
    //TODO
    if (array.size > 0) return array.arr[array.size - 1];
    else return Soldier();//return this if cannot get top
}

//////////////////////////////////////////////////////
/// TASK 2
//////////////////////////////////////////////////////

bool enqueue(SLinkedList& list, Soldier soldier){
    //Return true if enqueue successfully, false otherwise
    //TODO
    return insertAt(list, soldier, 0);
}

bool dequeue(SLinkedList& list){
    //Return true if dequeue successfully, false otherwise
    //TODO
    return removeAt(list, 0);
}

Soldier front(SLinkedList& list){
    //TODO
    if (empty(list)) return Soldier(); // return this if cannot get front
    return list.head->data;
}

//////////////////////////////////////////////////////
/// TASK 3
//////////////////////////////////////////////////////

void reverse(SLinkedList& list){
    if (list.head == NULL) return;
    SoldierNode* curr = list.head;
    SoldierNode* prev = NULL;
    SoldierNode* next = NULL;
    while (curr != NULL)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    list.head = curr;
}

//////////////////////////////////////////////////////
/// TASK 4
//////////////////////////////////////////////////////

SLinkedList merge(SLinkedList& list1, SLinkedList& list2){
    //TODO
    
    return SLinkedList();
}

//You can write your own functions here

//End your own functions

#endif /* thirdBattle_h */
