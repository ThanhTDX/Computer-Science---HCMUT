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
    if (array.size <= 0) return false;
    return false;
}

bool pop(Array& array){
    //Return true if pop successfully, false otherwise
    //TODO
    
    return false;
}

Soldier top(Array& array){
    //TODO
    
    return Soldier();//return this if cannot get top
}

//////////////////////////////////////////////////////
/// TASK 2
//////////////////////////////////////////////////////

bool enqueue(SLinkedList& list, Soldier soldier){
    //Return true if enqueue successfully, false otherwise
    //TODO
    
    return false;
}

bool dequeue(SLinkedList& list){
    //Return true if dequeue successfully, false otherwise
    //TODO
    
    return false;
}

Soldier front(SLinkedList& list){
    //TODO
    
    return Soldier();//Return this if cannot get front
}

//////////////////////////////////////////////////////
/// TASK 3
//////////////////////////////////////////////////////

void reverse(SLinkedList& list){
    //TODO
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
