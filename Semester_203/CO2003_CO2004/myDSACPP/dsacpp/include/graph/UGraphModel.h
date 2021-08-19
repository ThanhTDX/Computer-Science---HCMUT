/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   UGraphModel.h
 * Author: LTSACH
 *
 * Created on 24 August 2020, 15:16
 */

#ifndef UGRAPHMODEL_H
#define UGRAPHMODEL_H

#include "graph/AbstractGraph.h"
#include "stacknqueue/PriorityQueue.h"

//////////////////////////////////////////////////////////////////////
///////////// UGraphModel: Undirected Graph Model ////////////////////
//////////////////////////////////////////////////////////////////////


template<class T>
class UGraphModel: public AbstractGraph<T>{
private:
public:
    //class UGraphAlgorithm;
    //friend class UGraphAlgorithm;
    
    UGraphModel(
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
        if (from != to) toVertex->connect(fromVertex, weight);
    }
    void disconnect(T from, T to){
        if (!AbstractGraph<T>::connected(from, to) ||!AbstractGraph<T>::connected(to, from) ) return;
        typename AbstractGraph<T>::VertexNode* fromVertex = this->getVertexNode(from);
        typename AbstractGraph<T>::VertexNode* toVertex = this->getVertexNode(to);
        if (!fromVertex) throw VertexNotFoundException(this->vertex2Str(*fromVertex));
        if (!toVertex) throw VertexNotFoundException(this->vertex2Str(*toVertex));
        
        fromVertex->removeTo(toVertex);
        if (from != to)  toVertex->removeTo(fromVertex);
    }
    void remove(T vertex){
        //YOUR CODE HERE
        typename AbstractGraph<T>::VertexNode* deleteVertex = this->getVertexNode(vertex);
        if (!deleteVertex) throw VertexNotFoundException(this->vertex2Str(*deleteVertex));

        DLinkedList<T> vertices;
        typename DLinkedList<T>::Iterator vertexIt;
        
        ///////////////////////CLEAR IN - OUT EDGES
        vertices = this->getInwardEdges(vertex);
        for (vertexIt = vertices.begin(); vertexIt != vertices.end(); vertexIt++)
        {
            typename AbstractGraph<T>::VertexNode* node = this->getVertexNode(*vertexIt);
            node->removeTo(deleteVertex);
            deleteVertex->removeTo(node);
        }
        //////////////////////REMOVE NODE FROM GRAPH LIST
        this->nodeList.removeItem(deleteVertex);
    }
    static UGraphModel<T>* create(T* vertices, int ver_size, 
                            Edge<T>* edges, int edge_size,
                            bool (*vertexEQ)(T&, T&)=0,
                            string (*vertex2str)(T&)=0 )
    {
        UGraphModel<T>* newModel = new UGraphModel<T>(vertexEQ, vertex2str);
        for (int i = 0; i != ver_size; i++)
            newModel->add(vertices[i]);
        for (int i = 0; i != edge_size; i++)
            newModel->connect(edges[i].from, edges[i].to);
            
        return newModel;
    }
};



#endif /* UGRAPHMODEL_H */

