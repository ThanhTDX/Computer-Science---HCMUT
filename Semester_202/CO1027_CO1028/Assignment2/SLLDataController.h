//
//  SLLDataControler.h
//  KTLT ASS 3
//
//  Created by Nhân Nguyễn on 17/05/2021.
//

// Students can remove the final initial return of the functions

#ifndef SLLDataController_h
#define SLLDataController_h

#include "dataStructure.h"
#include <vector>
#include <string>

//Functions used to manage Singly Linked List
void print(SLinkedList& list){
    if (!list.size) {
        std::cout << "List is empty" << endl;
        return;
    }
    SoldierNode* head = list.head;
    while (head){
        std::cout << head->data.ID << "->";
        head = head->next;
    }
    std::cout << "NULL"<<endl;
}

bool empty(SLinkedList& list) {
    if (!list.size) return true;
    else return false;
}

int size(SLinkedList& list){   
    return list.size;
}

bool insertAt (SLinkedList& list, Soldier element, int pos){
    if (pos < 0 || pos > list.size - 1) return false;
    list.size++;
    SoldierNode* newSoldier = new SoldierNode(element, NULL);
    //Check if pos is 0 - insert at first element.
    if (pos == 0)
    {
        newSoldier->next = list.head;
        list.head = newSoldier;
        return true;
    }

    //Create a pointer to move
    SoldierNode* ptr = list.head;
    while (pos > 0)
    {
        ptr = ptr->next;
        pos--;
    }
    newSoldier->next = ptr->next;
    ptr->next = newSoldier;
    return true;
}

bool removeAt (SLinkedList& list, int idx){
    SoldierNode* ptr = list.head;
    //If 
    //+ idx invalid
    //+ idx > size (this checks if list is empty)
    if (idx < 0 ||idx > list.size - 1) return false;

    //idx = 0, delete the head
    if (idx == 0)
    {
        list.head = ptr->next;
        delete ptr;
        list.size--;
        return true;
    }

    //other cases (idx > list.size - 1 return false)
    while (idx > 1)
    {
        ptr = ptr->next;
        idx--;
    }
    SoldierNode* nextNode = ptr->next->next;
    delete ptr->next;
    ptr->next = nextNode;
    list.size--;
    return true;
}

bool removeFirstItemWithHP (SLinkedList& list, int HP){
    
    if (!size(list)) return false;
    SoldierNode* ptr = list.head;
    int count = 0;
    while (1)
    {
        if (ptr->data.HP == HP)
            return removeAt(list, count);
        if (ptr->next == NULL) return false;
        else ptr = ptr->next;
        count++;
    }
}

int indexOf(SLinkedList& list, Soldier soldier){
    //Find index of soldier (start from 0)
    //Return -1 if the soldier does not exist
    //TODO
    if (!size(list)) return -1;
    int count = 0;
    SoldierNode* ptr = list.head;
    while (1)
    {
        if (ptr->data.HP == soldier.HP && 
            ptr->data.ID == soldier.ID && 
            ptr->data.isSpecial == soldier.isSpecial)
            return count;
        if (!ptr->next) return -1;
        else ptr = ptr->next;
        count++;
    }
    return -2;
}

void clear(SLinkedList& list){
    if (!list.head) return;
    list.size = 0;
    while (1)
    {
        SoldierNode* ptr = list.head;
        list.head = ptr->next;
        delete ptr;
        if (!list.head) break;
    }
}

string getIDAt(SLinkedList& list, int pos){
    if (pos < 0 || pos > list.size - 1) return "-1";
    SoldierNode* ptr = list.head;
    while (pos > 0)
    {
        ptr = ptr->next;
        pos--;
    }
    return ptr->data.ID;
}

int getHPAt(SLinkedList& list, int pos){
    if (pos < 0 || pos > list.size - 1) return -1;
    SoldierNode* ptr = list.head;
    while (pos > 0)
    {
        ptr = ptr->next;
        pos--;
    }
    return ptr->data.HP;
}

bool setHPAt(SLinkedList& list, int HP, int pos){
    if (pos < 0 || pos > list.size - 1) return false;
    SoldierNode* ptr = list.head;
    while (pos > 0)
    {
        ptr = ptr->next;
        pos--;
    }
    ptr->data.HP = HP;
    return true;
}

bool contains (SLinkedList& list, Soldier soldier){
    if (!size(list)) return false;
    SoldierNode* ptr = list.head;
    while (1)
    {
        //Operator== (const Soldier& x, const Soldier& y); ?
        if (ptr->data.HP == soldier.HP && 
            ptr->data.ID == soldier.ID && 
            ptr->data.isSpecial == soldier.isSpecial)
            return true;
        if (!ptr->next) return false;
        else ptr = ptr->next;
    }
}

//You can write your own functions here
// 
//End your own functions

#endif /* SLLDataControler_h */
