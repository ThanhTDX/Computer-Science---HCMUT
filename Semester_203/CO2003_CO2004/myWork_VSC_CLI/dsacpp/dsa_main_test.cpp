#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include "doctest.h"
#include "test/SortTest.h"
#include "test/GraphTest.h"
//UNCOMMENT the following WHENEVER completing the related data structures
/*
#include "test/SLinkedListTest.h"
#include "test/SLinkedListSETest.h"
#include "test/DLinkedListTest.h"
#include "test/DLinkedListSETest.h"
#include "test/BSTTest.h"
#include "test/StackTest.h"
#include "test/QueueTest.h"
#include "test/HeapTest.h"
#include "test/PriorityQueueTest.h"
#include "test/XHashMapTest.h"
#include "test/SortTest.h"
#include "test/GraphTest.h"
#include "test/AVLTest.h"
*/

// //////////////////////////////////BORING SIDE PROJECT/////////////////////////////////////////
// //#define SAMPLE_TESTCASE
// #define GENERATE_TESTCASE

// #ifdef SAMPLE_TESTCASE
// #define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
// #include "doctest.h"

// //#include "test/XArrayListTest.h"
// //#include "test/XArrayListSETest.h"

// //UNCOMMENT the following WHENEVER completing the related data structures

// #include "test/SLinkedListTest.h"
// //#include "test/SLinkedListSETest.h"
// #include "test/DLinkedListTest.h"
// //#include "test/DLinkedListSETest.h"
// //#include "test/BSTTest.h"
// #include "test/StackTest.h"
// #include "test/QueueTest.h"
// //#include "test/HeapTest.h"
// //#include "test/PriorityQueueTest.h"
// //#include "test/XHashMapTest.h"
// //#include "test/SortTest.h"
// //#include "test/GraphTest.h"
// //#include "test/AVLTest.h"
// #endif

// #ifdef GENERATE_TESTCASE
// #include "include/list/XArrayList.h"
// #include "include/list/SLinkedList.h"
// #include "include/list/DLinkedList.h"

// #include <iostream>
// #include <vector>
// #include <time.h>
// using namespace std;

// /*
// Please read this instructions carfully
//     Note 1: Before compiling, remember to use the below code for toString() function
// of both SLinkedList.h and DLinkedList.h:
// //template <typename T>
// /*SLinkedList*/
// /*DLinkedList*/ /*::toString(string (*item2str)(T&) ){
//     if (count == 0) return "[]";

//     stringstream ss;
//     ss << "[";
//     Node* ptr = head->next;
//     while(ptr->next != tail){
//         if(item2str != 0) ss << item2str(ptr->data) << ", ";
//         else ss << ptr->data << ", ";
        
//         ptr = ptr->next;
//     }
//     if(item2str != 0) ss << item2str(ptr->data) << "]";
//     else ss << ptr->data << "]";

//     return ss.str();
// }*/
//                 /*
//     Note 2: You can change the macros below to use my code for different purpose.
//     Note 3: Each time you run this code, a number of random test cases will be generated,
// and the code on both SLinkedList.h and XArrayList.h (teacher's code) will be included. Your
// results will be compared with Mr.Sach's result.


// */

// ///////////////////////////////////////////////////////////////////////////////
// ///////////////////////////////////MACRO///////////////////////////////////////
// ///////////////////////////////////////////////////////////////////////////////
// #define TEST_NUM 5000  // the number of random test cases
// #define TEST_SIZE 40  // the number of operations for each test case
// #define RANDE_MAX 20 // the maximum value of the random elements that is used for the operations that need element values


// // #define SLINKEDLIST
// // Keep this macro if you want to check your code in SLinkedList.h. Remove it if you want
// // to check your code for DLinkedList.h instead

// vector<int> com, par1, par2;
// ///////////////////////////////////////////////////////////////////////////////
// ////////////////////////////////ALL FUNCTIONS//////////////////////////////////
// ///////////////////////////////////////////////////////////////////////////////
// template <class E, class G>
// void addItem(E &expected, G &got)
// {
//     int e = rand() % 50;
//     par1.push_back(e);
//     par2.push_back(-1);
//     expected.add(e);
//     got.add(e);
// }

// template <class E, class G>
// bool addItemIndex(E &expected, G &got, bool &threw)
// {
//     int index = rand() % (TEST_SIZE / 3 * 2);
//     par1.push_back(index);
//     int e = rand() % RANDE_MAX;
//     par2.push_back(e);
//     bool expected_error = false, got_error = false;

//     try
//     {
//         expected.add(index, e);
//     }
//     catch (std::out_of_range &)
//     {
//         expected_error = true;
//     }
//     try
//     {
//         got.add(index, e);
//     }
//     catch (std::out_of_range &)
//     {
//         got_error = true;
//     }

//     if (expected_error != got_error)
//     {
//         if (expected_error)
//             cout << "Your program should have thrown exception for add(int, T)" << endl;
//         else
//             cout << "Your program should not have thrown exception for add(int, T)" << endl;
//         return false;
//     }
//     else if (expected_error)
//         threw = true;
//     return true;
// }

// template <class E, class G>
// bool removeAt(E &expected, G &got, bool &threw)
// {
//     int index = rand() % (TEST_SIZE / 3 * 2);
//     par1.push_back(index);
//     par2.push_back(-1);
//     bool expected_error = false, got_error = false;

//     try
//     {
//         expected.removeAt(index);
//     }
//     catch (std::out_of_range &)
//     {
//         expected_error = true;
//     }
//     try
//     {
//         got.removeAt(index);
//     }
//     catch (std::out_of_range &)
//     {
//         got_error = true;
//     }

//     if (expected_error != got_error)
//     {
//         if (expected_error)
//             cout << "Your program should have thrown exception for removeAt(int)" << endl;
//         else
//             cout << "Your program should not have thrown exception for removeAt(int)" << endl;
//         return false;
//     }
//     else if (expected_error)
//         threw = true;
//     return true;
// }

// template <class E, class G>
// bool removeItem(E &expected, G &got)
// {
//     int item = rand() % RANDE_MAX;
//     par1.push_back(item);
//     par2.push_back(-1);
//     int ex = expected.removeItem(item);
//     int go = got.removeItem(item);
//     if (ex != go)
//     {
//         cout << "The return value of removeItem(int) function must be " << ex << " instead of " << go << endl;
//         return false;
//     }
//     else
//         return true;
// }

// template <class E, class G>
// bool get(E &expected, G &got, bool& threw)
// {
//     int index = rand() % (TEST_SIZE / 3);
//     par1.push_back(index);
//     par2.push_back(-1);
//     int ex, go;
//     bool expected_error = false, got_error = false;
//     try
//     {
//         ex = expected.get(index);
//     }
//     catch (std::out_of_range &)
//     {
//         expected_error = true;
//     }
//     try
//     {
//         go = got.get(index);
//     }
//     catch (std::out_of_range &)
//     {
//         got_error = true;
//     }
//     if (expected_error != got_error)
//     {
//         if (expected_error)
//             cout << "Your program should have thrown exception for get(int)" << endl;
//         else
//             cout << "Your program should not have thrown exception for get(int)" << endl;
//         return false;
//     }
//     else if (expected_error)
//         threw = true;
//     else if (ex != go)
//     {
//         cout << "The return value of get(int) function must be " << ex << " instead of " << go << endl;
//         return false;
//     }
//     return true;
// }

// template <class E, class G>
// bool indexOf(E &expected, G &got)
// {
//     int item = rand() % RANDE_MAX;
//     par1.push_back(item);
//     par2.push_back(-1);
//     int ex = expected.indexOf(item);
//     int go = got.indexOf(item);
//     if (ex != go)
//     {
//         cout << "The return value of indexOf(int) function must be " << ex << " instead of " << go << endl;
//         return false;
//     }
//     else
//         return true;
// }

// template <class E, class G>
// bool contains(E& expected, G &got)
// {
//     int item = rand() % RANDE_MAX;
//     par1.push_back(item);
//     par2.push_back(-1);
//     int ex = expected.contains(item);
//     int go = got.contains(item);
//     if (ex != go)
//     {
//         cout << "The return value of contains(int) function must be " << ex << " instead of " << go << endl;
//         return false;
//     }
//     else
//         return true;
// }
// ///////////////////////////////////////////////////////////////////////////////
// ////////////////////////////////END FUNCTIONS//////////////////////////////////
// ///////////////////////////////////////////////////////////////////////////////

// int main()
// {
//     srand(time(NULL));
//     XArrayList<int> expected;
//     #ifdef SLINKEDLIST
//         SLinkedList<int> got;
// #endif
// #ifndef SLINKEDLIST
//         DLinkedList<int> got;
// #endif
//     cout << "Generating testcase with T = int ....." << endl;
//     for (int test = 0; test < TEST_NUM; test++)
//     {
//         if (got.size() != 0)
//         {
//             cout << "Wrong output for size() function";
//             return 0;
//         }
//         for (int i = 0; i < TEST_SIZE; i++)
//         {
//             bool okay = true, threw = false;
//             com.push_back(rand() % 7);
//             switch (com[i])
//             {
//             case 0:
//             {
//                 addItem(expected, got);
//                 break;
//             }
//             case 1:
//             {
//                 okay = addItemIndex(expected, got, threw);
//                 break;
//             }
//             case 2:
//             {
//                 okay = removeAt(expected, got, threw);
//                 break;
//             }
//             case 3:
//             {
//                 okay = removeItem(expected, got);
//                 break;
//             }
//             case 4:
//             {
//                 okay = get(expected, got, threw);
//                 break;
//             }
//             case 5:
//             {
//                 okay = indexOf(expected, got);
//                 break;
//             }
//             case 6:
//             {
//                 okay = contains(expected, got);
//                 break;
//             }
//             }

//             if (expected.size() != got.size())
//             {
//                 cout << "Check your size() function. Remeber to add 1 for add functions and minus 1 for remove and removeAt functions" << endl;
//                 cout << "Got size(): " << got.size() << " - Expected size(): " << expected.size() << endl;
//                 return 0;
//             }
//             if (expected.toString() != got.toString() && !threw)
//                 okay = false;
//             if (!okay)
//             {
//                 cout << "Wrong answer at test case " << test << endl;
//                 cout << "Tasks: \n";
//                 for (int k = 0; k <= i; k++)
//                 {
//                     switch (com[k])
//                     {
//                     case 0:
//                         cout << "\tadd(" << par1[k] << ");\n";
//                         break;
//                     case 1:
//                         cout << "\tadd(" << par1[k] << ", " << par2[k] << ");\n";
//                         break;
//                     case 2:
//                         cout << "\tremoveAt(" << par1[k] << ");\n";
//                         break;
//                     case 3:
//                         cout << "\tremoveItem(" << par1[k] << ");\n";
//                         break;
//                     case 4:
//                         cout << "\tget(" << par1[k] << ");\n";
//                         break;
//                     case 5:
//                         cout << "\tindexOf(" << par1[k] << ");\n";
//                         break;
//                     case 6:
//                         cout << "\tcontains(" << par1[k] << ");\n";
//                         break;
//                     }
//                 }
//                 cout << "Wrong output since the last operation showed above" << endl;
//                 cout << "Expected:\n\t";
//                 expected.println();
//                 cout << "Got:\n\t";
//                 got.println();
//                 return 0;
//             }
//         }
//         std::cout << "Testcase " << test << " cleared.\n";
//         com.clear();    par1.clear();   par2.clear();
//         expected.clear();   got.clear();
//     }
//     cout << "Congratulations! You have passed all " << TEST_NUM << " random test cases." << endl;
//     return 0;
// }

// #endif