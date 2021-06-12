//
//  ArrayDataController.h
//  KTLT ASS 3
//
//  Created by Nhân Nguyễn on 17/05/2021.
//

// Students can remove the final initial return of the functions

#ifndef ArrayDataController_h
#define ArrayDataController_h

#include "dataStructure.h"
#include <vector>
#include <string>

//Functions used to manage Array
void print(Array& array){
    if (!array.size) {
        std::cout << "Array is empty" << endl;
        return;
    }
    std::cout <<"[";
    for(int i=0;i<array.size;i++){
        std::cout << array.arr[i].ID << " ";
    }
    std::cout <<"]" << endl;
}

void ensureCapacity(Array& array, int newCap) {
    //Check if capacity is full
    if (array.size > array.capacity)
    {
        //Create new array with newCap
        Soldier* temp = new Soldier[newCap];
        //Copy the data of old array to new array
        for (int i = 0; i < array.capacity; i++)
        {
            temp[i] = array.arr[i];
        }
        //Delete the old array
        delete[] array.arr;
        //Assign the pointer to new array
        array.arr = temp;
        //Update capacity
        array.capacity = newCap;
    }
    else;
}

bool empty(Array& array) {
    if (array.size == 0) return true;
    return false;
}

void initArray (Array& array, int cap){
    array.arr = new Soldier[cap];
    array.capacity = cap;
    array.size = 0;
}

bool insertAt(Array& array, Soldier element, int pos){
    if (pos < 0 || pos > array.size || array.arr == NULL) return false;
    
    //Since we add new element, must check if size > capacity
    array.size++;
    ensureCapacity(array, (array.capacity * 3) / 2 + 1);
    
    //move the elements on pos to the right, and add it.
    for (int idx = array.size - 1; idx > pos; idx--)
        array.arr[idx] = array.arr[idx-1];
    array.arr[pos] = element;
    
    return true;
};

bool removeAt (Array& array, int idx){
    if (idx < 0 || idx > array.size - 1 || empty(array)) return false;
    array.size--;
    if (array.size == 0);

    else for (int i = idx + 1; i <= array.size; i++)
        array.arr[i-1] = array.arr[i];
    return true;
}

bool removeFirstItemWithHP (Array& array, int HP){
    if (empty(array)) return false;
    for (int count = 0; count < array.size; count++)
    {
        if (array.arr[count].HP == HP)
            return removeAt(array, count);
    }
    return false;
}

int indexOf(Array& array, Soldier soldier){
    if (empty(array)) return -1;
    for (int tmp = 0; tmp < array.size; tmp++)
    {
        if (array.arr[tmp].HP == soldier.HP && 
            array.arr[tmp].ID == soldier.ID && 
            array.arr[tmp].isSpecial == soldier.isSpecial)
            return tmp;
    }
    return -1;
}

int size(Array& array){
    return array.size;
}

string getIDAt(Array& array, int pos){
    //Get ID of the Soldier at pos
    //TODO
    if (pos > array.size - 1) return "-1";
    return array.arr[pos].ID;
}

int getHPAt(Array& array, int pos){
    //Get HP of the Soldier at pos
    //TODO
    if (pos > array.size - 1) return -1;
    return array.arr[pos].HP;
}

bool setHPAt(Array& array, int HP, int pos){
    //Set value of HP at pos
    //TODO
    //Return true if set successfully, false otherwise
    if (pos > array.size - 1) return false;
    array.arr[pos].HP = HP;
    return true;;
}

void clear(Array& array){
    //Delete all of the elements in array
    //TODO
    delete[] array.arr;
    array.arr = NULL;
    array.size = 0;
    array.capacity = 0;
}

bool contains (Array& array, Soldier soldier){
    //Check if array contains soldier
    //TODO
    for (int pos = 0; pos < array.size; pos++)
    {
        if (array.arr[pos].HP == soldier.HP && 
            array.arr[pos].ID == soldier.ID &&
            array.arr[pos].isSpecial == soldier.isSpecial)
            return true;
    }
    return false;
}

//You can write your own functions here
//
//End your own functions

#endif /* ArrayDataController_h */
