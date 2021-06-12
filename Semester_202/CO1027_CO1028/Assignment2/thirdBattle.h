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
    //Note: push to the end of array
    if (array.arr == NULL) initArray(array, 0);
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
    return insertAt(list, soldier, list.size);
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
    list.head = prev;
}

//////////////////////////////////////////////////////
/// TASK 4
//////////////////////////////////////////////////////

//Function declaration
SLinkedList sortedList(SLinkedList& list);
bool compareNodes(SoldierNode* nodeLeft, SoldierNode* nodeRight);
void swapNodes(SoldierNode* node1, SoldierNode* node2);

SLinkedList merge(SLinkedList& list1, SLinkedList& list2){
    //TODO
    if (list1.head == NULL) return sortedList(list2);
    if (list2.head == NULL) return sortedList(list1);

    list1 = sortedList(list1);

    SoldierNode* ptr = list1.head;
    while (ptr->next != NULL)
        ptr = ptr->next;
    ptr->next = list2.head;
    return sortedList(list1);
}

SLinkedList sortedList(SLinkedList& list){
    while(1){
        bool doChange = false;
        SoldierNode* ptr = list.head;
        while (ptr->next != NULL){
            if (compareNodes(ptr, ptr->next)){
                doChange = true;
                swapNodes(ptr, ptr->next);
            }
            else ptr = ptr->next;
        }
        if (!doChange) break;
    }
    return list;
}

//This function is written according to the requirements
bool compareNodes(SoldierNode* nodeLeft, SoldierNode* nodeRight)
{
    if (nodeLeft->data.HP < nodeRight->data.HP) return false;
    else if (nodeLeft->data.HP > nodeRight->data.HP) return true;
    else if (nodeLeft->data.HP == nodeRight->data.HP)
    {
        if (nodeLeft->data.isSpecial < nodeRight->data.isSpecial) return false;
        else if (nodeLeft->data.isSpecial > nodeRight->data.isSpecial) return true;
        else if (nodeLeft->data.isSpecial == nodeRight->data.isSpecial) 
        {
            if (nodeLeft->data.ID <= nodeRight->data.ID) return false;
            else return true;
        }
    }
    return false;
}
void swapNodes(SoldierNode* node1, SoldierNode* node2)
{
    //Basically swapping data inside two nodes.
    Soldier temp = node1->data;
    node1->data = node2->data;
    node2->data = temp;
}
//You can write your own functions here

//End your own functions

#endif /* thirdBattle_h */
