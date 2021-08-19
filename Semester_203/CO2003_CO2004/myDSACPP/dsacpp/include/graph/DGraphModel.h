/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   DGraphModel.h
 * Author: LTSACH
 *
 * Created on 23 August 2020, 19:36
 */

#ifndef DGRAPHMODEL_H
#define DGRAPHMODEL_H
#include "graph/AbstractGraph.h"
#include "stacknqueue/Queue.h"
#include "stacknqueue/Stack.h"
#include "hash/XHashMap.h"
#include "stacknqueue/PriorityQueue.h"
#include "sorting/DLinkedListSE.h"


//////////////////////////////////////////////////////////////////////
///////////// GraphModel: Directed Graph Model    ////////////////////
//////////////////////////////////////////////////////////////////////


template<class T>
class DGraphModel: public AbstractGraph<T>{
private:
public:
    DGraphModel(
            bool (*vertexEQ)(T&, T&), 
            string (*vertex2str)(T&) ): 
        AbstractGraph<T>(vertexEQ, vertex2str){
    }
    
    void connect(T from, T to, float weight=0){
        //YOUR CODE HERE
        typename AbstractGraph<T>::VertexNode* fromVertex = this->getVertexNode(from);
        typename AbstractGraph<T>::VertexNode* toVertex = this->getVertexNode(to);
        if (!fromVertex) throw VertexNotFoundException(this->vertex2Str(*fromVertex));
        if (!toVertex) throw VertexNotFoundException(this->vertex2Str(*toVertex));
        fromVertex->connect(toVertex, weight);
    }
    void disconnect(T from, T to){
        //YOUR CODE HERE
        if (!AbstractGraph<T>::connected(from, to)) return;
        typename AbstractGraph<T>::VertexNode* fromVertex = this->getVertexNode(from);
        typename AbstractGraph<T>::VertexNode* toVertex = this->getVertexNode(to);
        if (!fromVertex) throw VertexNotFoundException(this->vertex2Str(*fromVertex));
        if (!toVertex) throw VertexNotFoundException(this->vertex2Str(*toVertex));

        fromVertex->removeTo(toVertex);
    }
    void remove(T vertex){
        //YOUR CODE HERE
        typename AbstractGraph<T>::VertexNode* deleteVertex = this->getVertexNode(vertex);
        if (!deleteVertex) throw VertexNotFoundException(this->vertex2Str(*deleteVertex));

        DLinkedList<T> vertices;
        typename DLinkedList<T>::Iterator vertexIt;
        
        ///////////////////////CLEAR IN  EDGES
        vertices = this->getInwardEdges(vertex);
        for (vertexIt = vertices.begin(); vertexIt != vertices.end(); vertexIt++)
        {
            typename AbstractGraph<T>::VertexNode* node = this->getVertexNode(*vertexIt);
            node->removeTo(deleteVertex);
        }
        ///////////////////////CLEAR OUT EDGES
        vertices = this->getOutwardEdges(vertex);
        for (vertexIt = vertices.begin(); vertexIt != vertices.end(); vertexIt++)
        {
            typename AbstractGraph<T>::VertexNode* node = this->getVertexNode(*vertexIt);
            deleteVertex->removeTo(node);
        }
        //////////////////////REMOVE NODE FROM GRAPH LIST
        this->nodeList.removeItem(deleteVertex);
    }
    static DGraphModel<T>* create(T* vertices, int ver_size, 
                            Edge<T>* edges, int edge_size,
                            bool (*vertexEQ)(T&, T&)=0,
                            string (*vertex2str)(T&)=0 )
    {
        DGraphModel<T>* newModel = new DGraphModel<T>(vertexEQ, vertex2str);
        for (int i = 0; i != ver_size; i++)
            newModel->add(vertices[i]);
        for (int i = 0; i != edge_size; i++)
            newModel->connect(edges[i].from, edges[i].to);
        return newModel;
    }
};

#endif /* DGRAPHMODEL_H */

