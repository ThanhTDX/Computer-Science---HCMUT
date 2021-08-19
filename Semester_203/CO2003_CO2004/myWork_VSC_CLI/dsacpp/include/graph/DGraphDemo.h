/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   DGraphDemo.h
 * Author: LTSACH
 *
 * Created on 23 August 2020, 20:26
 */

#ifndef DGRAPHDEMO_H
#define DGRAPHDEMO_H
#include "graph/DGraphModel.h"
#include "graph/TopoSorter.h"

bool charComparator(char& lhs, char& rhs){
    return lhs==rhs;
}
string vertex2str(char& v){
    stringstream os;
    os << v;
    return os.str();
}
void DGraphDemo1(){
    DGraphModel<char> model(&charComparator, &vertex2str);
    char vertices[] = {'A', 'B', 'C', 'D'};
    for(int idx=0; idx < 4; idx++){
        model.add(vertices[idx]);
    }
    model.connect('A', 'B');
    model.connect('B', 'D');
    model.connect('C', 'B');
    model.connect('C', 'D');
    model.println();
    // model.remove('B');
    // model.println();
}

void DGraphDemo2(){
    DGraphModel<char> model(&charComparator, &vertex2str);
    char vertices[] = {'A', 'B', 'C', 'D'};
    for(int idx=0; idx < 4; idx++){
        model.add(vertices[idx]);
    }
    model.connect('A', 'B');
    model.connect('B', 'D');
    model.connect('C', 'B');
    model.connect('C', 'D');
    model.println();
    
    TopoSorter<char> sorter(&model);
    DLinkedList<char> topo = sorter.sort(TopoSorter<char>::BFS);
    cout << left << setw(15) << "Topo-order: " << topo.toString() << endl;
}


void DGraphDemo3(){
    DGraphModel<char> model(&charComparator, &vertex2str);
    for(int idx=0; idx<10; idx++){
        model.add((char)('0' + idx));
    }

    model.connect('0', '1');
    model.connect('0', '5');
    model.connect('1', '7');
    model.connect('3', '2');
    model.connect('3', '4');
    model.connect('3', '7');
    model.connect('3', '8');
    model.connect('4', '8');
    model.connect('6', '0');
    model.connect('6', '1');
    model.connect('6', '2');
    model.connect('8', '2');
    model.connect('8', '7');
    model.connect('9', '4');
    model.println();
    
    TopoSorter<char> sorter(&model);
    DLinkedList<char> bfs = sorter.sort(TopoSorter<char>::BFS);
    cout << left << setw(15) << "Topo-order (BFS): " << bfs.toString() << endl;
    
    DLinkedList<char> dfs = sorter.sort(TopoSorter<char>::DFS);
    cout << left << setw(15) << "Topo-order (DFS): " << dfs.toString() << endl;
}

template<class T>
bool comparator(T& lhs, T& rhs)
{
    return (lhs == rhs);
}

void DGraphDemo4(){
    char vertices[] = {'B', 'E', 'A', 'M', 'J'};
    Edge<char> edges[] = {
        Edge<char>('B', 'A'),
        Edge<char>('E', 'A'),
        Edge<char>('A', 'M'),
        Edge<char>('A', 'J')
    };
    DGraphModel<char> model(&comparator<char>, vertex2str);
    for(char v: vertices) model.add(v);
    for(Edge<char> e: edges) model.connect(e.from, e.to, e.weight);
    model.println();
}

void DGraphDemo5(){
    char vertices[] = {'B', 'E', 'A', 'M', 'J'};
    Edge<char> edges[] = {
        Edge<char>('B', 'A'),
        Edge<char>('E', 'A'),
        Edge<char>('A', 'M'),
        Edge<char>('A', 'J')
    };
    DGraphModel<char>* model = DGraphModel<char>::create(
                vertices, //pointer to the first vertex in an array of vertices
                5, //number of vertices in the array
                edges, //pointer to the first edge in an array of edges
                4, //number of edges in the array
                &comparator<char>, //pointer to a function for checking the equality of two vertices
                &vertex2str //pointer to a function for converting vertices to string
    );
    model->println();
    delete model;
}

// void dijkstraDemo(){
//     DGraphModel<char> model(&charComparator, &vertex2str);
//     model.add('0');
//     model.add('1');
//     model.add('2');
//     model.add('3');
//     model.add('4');
//     model.connect('0', '1', 5);
//     model.connect('0', '2', 3);
//     model.connect('0', '4', 2);

//     model.connect('1', '2', 2);
//     model.connect('1', '3', 6);

//     model.connect('2', '1', 1);
//     model.connect('2', '3', 2);

//     model.connect('4', '1', 6);
//     model.connect('4', '2', 10);
//     model.connect('4', '3', 4);
//     model.println();
 

//     DGraphAlgorithm<char> finder;
//     DLinkedList<Path<char>*> list = finder.dijkstra(&model, '0');
//     cout << "Dijkstra output:" << endl;
//     for(DLinkedList<Path<char>*>::Iterator it= list.begin(); it != list.end(); it++){
//         Path<char>* path = *it;
        
//         cout << left << setw(8) << "path: ";
//         cout << path->toString() << endl;
//     }
//     cout << endl;
// }


#endif /* DGRAPHDEMO_H */

