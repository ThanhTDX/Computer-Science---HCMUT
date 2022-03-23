/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   SLinkedList.h
 * Author: LTSACH
 *
 * Created on 19 August 2020, 16:56
 */

#ifndef SLINKEDLIST_H
#define SLINKEDLIST_H

#include "list/IList.h"

#include <sstream>
#include <iostream>
#include <type_traits>
using namespace std;

template <class T> class SLinkedList;

template<class T>
class SLinkedList: public IList<T> {
public:
    class Iterator; //forward declaration
    class Node; //forward declaration
    
protected:
    Node *head; //this node does not contain user's data
    Node *tail; //this node does not contain user's data
    int  count;  //keep number of items stored in the list
    bool (*itemEqual)(T& lhs, T& rhs);
    void (*deleteUserData)(SLinkedList<T>*);
    
public:
    SLinkedList(
            void (*deleteUserData)(SLinkedList<T>*)=0, 
            bool (*itemEqual)(T&, T&)=0);
    SLinkedList(const SLinkedList<T>& list);
    SLinkedList<T>& operator=(const SLinkedList<T>& list);
    ~SLinkedList();
    
    //Inherit from IList: BEGIN
    void    add(T e);
    void    add(int index, T e);
    T       removeAt(int index);
    bool    removeItem(T item, void (*removeItemData)(T)=0);
    bool    empty();
    int     size();
    void    clear();
    T&      get(int index);
    int     indexOf(T item);
    bool    contains(T item);
    string  toString(string (*item2str)(T&)=0 );
    //Inherit from IList: END
    void    bubbleSort();
    
    void println(string (*item2str)(T&)=0 ){
        cout << toString(item2str) << endl;
    }
    void setDeleteUserDataPtr(void (*deleteUserData)(SLinkedList<T>*) = 0){
        this->deleteUserData = deleteUserData;
    }

    Iterator begin(){
        return Iterator(this, true);
    }
    Iterator end(){
        return Iterator(this, false);
    }
    
    static void free(SLinkedList<T> *list){
        typename SLinkedList<T>::Iterator it = list->begin();
        while(it != list->end()){
            delete *it;
            it++;
        }
    }


protected:
    static bool equals(T& lhs, T& rhs, bool (*itemEqual)(T&, T& )){
        if(itemEqual == 0) return lhs == rhs;
        else return itemEqual(lhs, rhs);
    }
    
    void copyFrom(const SLinkedList<T>& list);
    void removeInternalData();
       
//////////////////////////////////////////////////////////////////////
////////////////////////  INNER CLASSES DEFNITION ////////////////////
//////////////////////////////////////////////////////////////////////   
public:
    class Node{
    public:
        T data;
        Node *next;
    public:
        Node(Node *next=0){
            this->next = next;
        }
        Node(T data, Node *next=0){
            this->data = data;
            this->next = next;
        }
    };
    
    //////////////////////////////////////////////////////////////////////
    //Iterator
    class Iterator{
    private:
        SLinkedList<T>* pList;
        Node* pNode;
        
    public:
        Iterator(SLinkedList<T>* pList=0, bool begin=true){
            if(begin){
                if(pList !=0) this->pNode = pList->head->next;
                else pNode = 0;
            }
            else{
                if(pList !=0) this->pNode = pList->tail;
                else pNode = 0;
            }
            this->pList = pList;
        }
        
        Iterator& operator=(const Iterator& iterator){
            this->pNode = iterator.pNode;
            this->pList = iterator.pList;
            return *this;
        }
        /*
         * remove: slow, O(n), why?
         * while-loop can have n iterations
         * => Use DLinkedList when need a linked-list
         */
        void remove(void (*removeItemData)(T)=0){
            Node* pCur = this->pList->head->next;
            Node* pPrev = this->pList->head;
            bool found = false;
            while(pCur != this->pList->tail){
                found = SLinkedList<T>::equals(pNode->data, pCur->data, pList->itemEqual);
                if(found){
                    //detach
                    pPrev->next = pCur->next;
                    if(pList->tail->next == pCur) pList->tail->next = pPrev; //update tail if needed
                    pList->count -= 1; //dec count in list
                    pCur->next = 0;

                    //remove users data + node :
                    if(removeItemData != 0) removeItemData(pCur->data);
                    delete pCur; 
                    
                    //prepare for next iteration, usually: it++
                    
                    this->pNode = pPrev;
                    
                    return;
                }
                
                //go next:
                pCur = pCur->next;
                pPrev = pPrev->next;
            }//while
        }
        
        T& operator*(){
            return pNode->data;
        }
        bool operator!=(const Iterator& iterator){
            return pNode != iterator.pNode;
        }
        // Prefix ++ overload 
        Iterator& operator++(){
            pNode = pNode->next;
            return *this; 
        }
        // Postfix ++ overload 
        Iterator operator++(int){
            Iterator iterator = *this; 
            ++*this; 
            return iterator; 
        }
    
    };
};


//////////////////////////////////////////////////////////////////////
////////////////////////     METHOD DEFNITION      ///////////////////
//////////////////////////////////////////////////////////////////////


template<class T>
SLinkedList<T>::SLinkedList(
        void (*deleteUserData)(SLinkedList<T>*), 
        bool (*itemEqual)(T&, T&) ) {
    head = new Node();
    tail = new Node();
    head->next = tail; tail->next = head;
    count = 0;
    this->itemEqual = itemEqual;
    this->deleteUserData = deleteUserData;
}

template<class T>
void SLinkedList<T>::copyFrom(const SLinkedList<T>& list){
    //Initialize this list to the empty condition
    this->count = 0;
    this->head->next = this->tail; this->tail->next = this->head;

    //Copy pointers from "list"
    this->deleteUserData = list.deleteUserData;
    this->itemEqual = list.itemEqual;

    //Copy data from "list"
    Node* ptr= list.head->next;
    while(ptr != list.tail){
        this->add(ptr->data);
        ptr = ptr->next;
    }
}

template<class T>
void SLinkedList<T>::removeInternalData(){
    //Remove user's data of this list
    if(deleteUserData != 0) deleteUserData(this);
    
    //Remove this list's data (i.e. Node)
    if((head != 0) & (tail != 0)){
        Node* ptr = head->next;
        while(ptr != tail){
            Node* next = ptr->next;
            delete ptr;
            ptr = next;
        }
    }
}
    
template<class T>
SLinkedList<T>::SLinkedList(const SLinkedList<T>& list){
    //Initialize to the empty condition
    //YOUR CODE HERE:  create two dummy nodes: head and tail
    head = new Node(NULL);
    tail = new Node(NULL);
    copyFrom(list);
}

template<class T>
SLinkedList<T>& SLinkedList<T>::operator=(const SLinkedList<T>& list){
    removeInternalData();
    copyFrom(list);
            
    return *this;
}

template<class T>
SLinkedList<T>::~SLinkedList() {
    removeInternalData();
    //YOUR CODE HERE: delete dummy nodes
    delete head;
    delete tail;
}

template<class T>
void SLinkedList<T>::add(T e) {
    Node* node = new Node(e, tail);
    if (node == NULL) throw "Overflow";
    tail->next->next = node;
    tail->next = node;
    count++;
}
template<class T>
void SLinkedList<T>::add(int index, T e) {
    if((index < 0) || (index > count))
        throw std::out_of_range("The index is out of range!");
    //index in [0, count]
    Node* newNode = new Node(e, 0);
    //Overflow checking
    if (newNode == NULL) throw "Overflow";

    //YOUR CODE HERE
    /* e = 40
    index = 1:
         ptr
          |
          v
    head->20->10->90->tail => head->20->40->10->90->tail

    index = 2:
             ptr
              |
              v
    head->20->10->90->tail => head->20->10->40->90->tail

    index = 3:
                 ptr
                  |
                  v
    head->20->10->90->tail => head->20->10->90->40->tail
    */
    Node* ptr = head;
    int ctr = 0;
    while (ctr != index)
    {
        ptr = ptr->next;
        ctr++;
    }
    newNode->next = ptr->next;
    ptr->next = newNode;
    //Change tail->next if needed
    if(index == count)
        tail->next = newNode;
    count += 1;
}
template<class T>
T SLinkedList<T>::removeAt(int index){
    if((index < 0) || (index > count - 1))
        throw std::out_of_range("The index is out of range!");

    //YOUR CODE HERE
    
    Node *ptr = head;
    while (index != 0)
    {
        ptr = ptr->next;
        index--;
    }
    
    T result = ptr->next->data;          //For output
    Node *nextNode = ptr->next->next;  
    delete ptr->next;
    ptr->next = nextNode;
    count--;

    //check if nextNode is at tail
    if (nextNode == tail)
        tail->next = ptr;
    return result;
}

template<class T>
bool SLinkedList<T>::removeItem(T item, void (*removeItemData)(T)){
    //YOUR CODE HERE
    Node *ptr = head->next;
    bool found = false;
    while (ptr->next != tail)
    {
        /*  itemEqual: if data is a pointer. if not do basic comparison
        
            static bool equals(T& lhs, T& rhs, bool (*itemEqual)(T&, T& )){
                if(itemEqual == 0) return lhs == rhs;
                else return itemEqual(lhs, rhs);
            }
        */
        found = SLinkedList<T>::equals(ptr->next->data, item, this->itemEqual);
        if(found)
        {
            /*  removeItemData: if data is a pointer,
                delete the whole object the pointer points too
                else do nothing.

                static void free(SLinkedList<T> *list){
                    typename SLinkedList<T>::Iterator it = list->begin();
                    while(it != list->end()){
                        delete *it;
                        it++;
                    }       
                }
            }*/
            if (removeItemData) removeItemData(ptr->next->data);
            Node *nextNode = ptr->next->next;  
            delete ptr->next;
            ptr->next = nextNode;
            count--;
            if (nextNode == tail)
                tail->next = ptr;
            return true;
        }
        ptr = ptr->next;
    }
    return false;
}

template<class T>
bool SLinkedList<T>::empty(){
    //YOUR CODE HERE
    return (count == 0);
}

template<class T>
int  SLinkedList<T>::size(){
    //YOUR CODE HERE
    return count;
}

template<class T>
void SLinkedList<T>::clear(){
    removeInternalData();
    //YOUR CODE HERE
    //Put the list to the initial condition (default constructor)
    head->next = tail;
    tail->next = head;
    count = 0;
}

template<class T>
T& SLinkedList<T>::get(int index){
    if((index < 0) || (index > count - 1))
        throw std::out_of_range("The index is out of range!");
    //YOUR CODE HERE
    Node *ptr = head->next;
    while (index != 0)
    {
        index--;
        ptr = ptr->next;
    }
    return ptr->data;
}

template<class T>
int  SLinkedList<T>::indexOf(T item){
    //YOUR CODE HERE
    int result = 0;
    Node *ptr = head->next;
    while (ptr != tail)
    {
        if (SLinkedList<T>::equals(ptr->data, item, this->itemEqual)) return result;
        ptr = ptr->next;
        result++;
    }
    return -1;
}
template<class T>
bool SLinkedList<T>::contains(T item){
    //YOUR CODE HERE
    return (indexOf(item) != -1);
}

template<class T>
string SLinkedList<T>::toString(string (*item2str)(T&) ){
    if (this->count == 0) return "[]";
    stringstream ss;
    Node* ptr = head->next;
    while(ptr != tail){
        if(item2str != 0) ss << item2str(ptr->data) << ", ";
        else ss << ptr->data << ", ";
        
        ptr = ptr->next;
    }
    
    if(count > 0){
        if(item2str != 0) ss << item2str(ptr->data);
        else ss << ptr->data;
    }
    
    //remove the last ", "
    string itemstr = ss.str();
    itemstr = itemstr.substr(0, itemstr.rfind(','));
    return "[" + itemstr + "]";
}

#endif /* SLINKEDLIST_H */
