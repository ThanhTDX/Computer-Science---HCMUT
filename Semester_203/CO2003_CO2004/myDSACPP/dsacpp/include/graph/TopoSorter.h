/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   TopoSorter.h
 * Author: ltsach
 *
 * Created on July 11, 2021, 10:21 PM
 */

#ifndef TOPOSORTER_H
#define TOPOSORTER_H
#include "graph/DGraphModel.h"

template<class T>
class TopoSorter{
public:
    static int DFS;
    static int BFS; 
    
protected:
    DGraphModel<T>* graph;
    int (*hash_code)(T&, int);
    
public:
    TopoSorter(DGraphModel<T>* graph, int (*hash_code)(T&, int)=0){
        this->graph = graph;
        this->hash_code = hash_code;
    }   
    DLinkedList<T> sort(int mode=0){
        if(mode == DFS) return dfsSort();
        else return bfsSort();
    }
    DLinkedList<T> bfsSort(bool shouldSort = true){
        DLinkedList<T> topoOrder;
        //YOUR CODE HERE
        XHashMap<T, int> indegreeMap = vertex2inDegree();
        DLinkedList<T> list0Degres = listOfZeroInDegrees();
        if(shouldSort && list0Degres.size() != 0) list0Degres.sort();

        Queue<T> open;

        for (typename DLinkedList<T>::Iterator it = list0Degres.begin(); it != list0Degres.end(); it++)
            open.push(*it);

        while (!open.empty())
        {
            T vertex = open.pop();
            topoOrder.add(vertex);
            DLinkedList<T> children = this->graph->getOutwardEdges(vertex);
            if(shouldSort && children.size() != 0) children.sort();
            for(typename DLinkedList<T>::Iterator childIt = children.begin(); childIt != children.end(); childIt++)
            {
                T child = *childIt;
                if(open.contains(child)) continue; 
                if(topoOrder.contains(child)) continue;

                int new_indeg = indegreeMap.get(child) - 1;
                indegreeMap.put(child, new_indeg);
                if (new_indeg == 0) open.push(child);
            }
        }
        return topoOrder;
    }
    
    DLinkedList<T> dfsSort(bool shouldSort = true){
        //YOUR CODE HERE
        DLinkedList<T> topoOrder;
        XHashMap<T, int> outdegreeMap = vertex2outDegree();
        DLinkedList<T> list0Degres = listOfZeroInDegrees();
        if(shouldSort && list0Degres.size() != 0) list0Degres.sort();

        Stack<T> open;
        for (typename DLinkedList<T>::Iterator it = list0Degres.begin(); it != list0Degres.end(); it++)
            open.push(*it);

        while (!open.empty())
            {
                T vertex = open.peek();
                int outDegree = outdegreeMap.get(vertex);
                if (outDegree == 0)
                {
                    open.pop();
                    topoOrder.add(0, vertex);
                }
                else
                {
                    DLinkedList<T> children = this->graph->getOutwardEdges(vertex);
                    if(shouldSort && children.size() != 0) children.sort();
                    for(typename DLinkedList<T>::Iterator childIt = children.begin(); childIt != children.end(); childIt++)
                    {                        
                        T child = *childIt;
                        if(topoOrder.contains(child)) continue;

                        if(open.contains(child))
                            open.remove(child);
                        open.push(child);
                    }
                    outdegreeMap.put(vertex, 0);
                }
                
            }
        return topoOrder;
    }
protected:
    XHashMap<T, int> vertex2inDegree(){
        //OLD XHashMap<T, int> map(&XHashMap<T, int>::simpleHash);
        //NEW// 
        XHashMap<T, int> map(this->hash_code);
        typename AbstractGraph<T>::Iterator vertexIt = this->graph->begin();
        while(vertexIt != this->graph->end()){
            T vertex = *vertexIt;
            int inDegree = this->graph->inDegree(vertex);
            map.put(vertex, inDegree);
            
            vertexIt++;
        }
        return map;
    }
    XHashMap<T, int> vertex2outDegree(){
        //OLD XHashMap<T, int> map(&XHashMap<T, int>::simpleHash);
        //NEW// 
        XHashMap<T, int> map(this->hash_code);
        typename AbstractGraph<T>::Iterator vertexIt = this->graph->begin();
        while(vertexIt != this->graph->end()){
            T vertex = *vertexIt;
            int outDegree = this->graph->outDegree(vertex);
            map.put(vertex, outDegree);
            
            vertexIt++;
        }
        return map;
    }
    
    DLinkedList<T> listOfZeroInDegrees(){
        DLinkedList<T> list;
        typename AbstractGraph<T>::Iterator vertexIt = this->graph->begin();
        while(vertexIt != this->graph->end()){
            T vertex = *vertexIt;
            int inDegree = this->graph->inDegree(vertex);
            if(inDegree == 0) list.add(vertex);
            
            vertexIt++;
        }
        return list;
    }
}; //TopoSorter
template<class T>
int TopoSorter<T>::DFS = 0;
template<class T>
int TopoSorter<T>::BFS = 1;

/////////////////////////////End of TopoSorter//////////////////////////////////


#endif /* TOPOSORTER_H */

