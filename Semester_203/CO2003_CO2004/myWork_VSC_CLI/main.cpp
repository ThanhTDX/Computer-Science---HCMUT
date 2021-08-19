#include <iostream>

#include <iomanip>

//MUST HAVE - MUST PUT AT THE BEGINNING
#include "util/Point.h"
#include "util/ArrayLib.h"
#include "geom/Point3D.h"
#include "geom/Vector3D.h"



// #include "list/XArrayListDemo.h"    //TESTED, FINISHED
#include "list/SLinkedListDemo.h"   //TESTED, FINISHED
// #include "list/DLinkedListDemo.h"   //TESTED, FINISHED
// #include "stacknqueue/QueueDemo.h"  //TESTED, FINISHED
// #include "stacknqueue/StackDemo.h"  //TESTED, FINIHSED
// #include "tree/BSTDemo.h"           //TESTED, FINIHSED
// #include "tree/AVLDemo.h"           //TESTED, FINIHSED
// #include "heap/HeapDemo.h"          //TESTED, FINISHED
// #include "hash/XHashMapDemo.h"      //NOT FINISHED
#include "graph/DGraphDemo.h"
#include "graph/UGraphDemo.h"


//SORTING PACK
#include "sorting/BubbleSortDemo.h"             //DONE
#include "sorting/StraightInsertionSortDemo.h"  //DONE
#include "sorting/HeapSortDemo.h"               //DONE
#include "sorting/StraightSelectionSortDemo.h"  //DONE
#include "sorting/QuickSortDemo.h"              //DONE
#include "sorting/ShellSortDemo.h"              //DONE
#include "sorting/ListSortDemo.h"               //DONE

using namespace std;

int main(int argc, char** argv) {
    std::cout << "\nSListDemo:\n";
    slistDemo6();
    return 0;
}



