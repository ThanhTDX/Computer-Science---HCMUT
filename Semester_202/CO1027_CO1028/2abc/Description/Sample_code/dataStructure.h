//
//  finalFight.h
//  KTLT ASS 3
//
//  Created by Nhân Nguyễn on 16/05/2021.
//
#include <iostream>
#include <string>
#include <vector>
using namespace std;

#ifndef dataStructure_h
#define dataStructure_h

struct Soldier{
    Soldier(): HP(-1), isSpecial(false), ID("") {}
    Soldier(int HP, int isSpecial, string ID): HP(HP), isSpecial(isSpecial), ID(ID) {}
    
    int HP;
    bool isSpecial;
    string ID;
};
//Soldier and SoldierNode? What do they do?
struct SoldierNode{
    SoldierNode(): data(Soldier()), next(NULL) {}
    SoldierNode(Soldier data, SoldierNode* next): data(data), next(next) {}
    
    Soldier data;
    SoldierNode* next;
};
//Of course, the start of the linked list.
struct SLinkedList{
    SLinkedList(): head(NULL), size(0) {}
    SLinkedList(SoldierNode* head, int size): head(head), size(size) {}
    
    SoldierNode* head;
    int size;
};
//So, besides a linked list, you'll create an array with capacity, ON THE STACK, to compare with Linked List (nice)
struct Array{
    Array(): arr(NULL), size(0), capacity(0) {}
    
    Soldier* arr;
    int size;
    int capacity;
};

vector<string> tokenize (string s, string del = " "){
    //Used for testcase tokenizer, students don't need to take care of this function.
    vector<string> res;
    int start = 0;
    int end = (int)s.find(del);
    while (end != -1) {
        res.push_back(s.substr(start, end - start));
        start = (int)end + (int)del.size();
        end = (int)s.find(del, start);
    }
    res.push_back(s.substr(start, end - start));
    return res;
}
//So this is basically turn a string to a vector. Nice we don't have to do it then
#endif /* dataStructure_h */
