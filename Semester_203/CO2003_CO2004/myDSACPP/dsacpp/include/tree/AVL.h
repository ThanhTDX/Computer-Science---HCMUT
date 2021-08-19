/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   AVL.h
 * Author: LTSACH
 *
 * Created on 12 September 2020, 17:11
 */

#ifndef AVL_H
#define AVL_H

#include "tree/BST.h"
#include "list/DLinkedList.h"
#include "stacknqueue/Queue.h"

#define XNode typename BST<K,V>::Node


template<class K, class V>
class AVL : public BST<K,V>{
public:
    void add(K key, V value=0){
        this->pRoot = add(this->pRoot, new XNode(typename BST<K,V>::Entry(key, value)));
        this->count += 1;
    }
    V remove(K key, bool* success=0){
        V retValue = 0; //O: NULL
        bool success_;
        this->pRoot = remove(this->pRoot, key, success_, retValue);
        if(success_) this->count -= 1;
        if(success != 0) *success = success_;
        return retValue;
    }
    int height(){
        if(this->pRoot == 0) return 0;
        return this->pRoot->height();
    }
    void println(string (*entry2str)(K&,V&)=0){
        cout << "Tree height: " << this->height() << endl;
        cout << "Tree nodes:"  << endl;
        cout << this->toString(entry2str, true) << endl;
    }
    /*
     * bfactor: designed for being used to test AVL tree
     *          so, maybe not useful for real application
     * It returns a list of balance factor (string) of nodes visited with BFS-traversal
     * (see AVLTest for example)
     */
    DLinkedList<string> bfactor(){
        DLinkedList<string> list;
        if(this->pRoot == 0) return list;
        
        Queue<XNode*> queue;
        queue.push(this->pRoot);
        while(!queue.empty()){
            XNode* pNode = queue.pop();
            if(pNode->bfactor == nEMPTY) list.add("EMPTY");
            else if(pNode->bfactor == nLH) list.add("LH");
            else if(pNode->bfactor == nEH) list.add("EH");
            else list.add("RH");
            
            if(pNode->bfactor == nEMPTY){
                delete pNode; //because alloc in [1] or [2]
                continue;
            } 
            if((pNode->pLeft == 0) && (pNode->pRight == 0) ) continue;
            
            if(pNode->pLeft != 0) queue.push(pNode->pLeft);
            else queue.push(new XNode()); //[1]
            if(pNode->pRight != 0) queue.push(pNode->pRight);
            else queue.push(new XNode()); //[2]
        }
        return list;
    }
private:
    /*
     Current tree:
                    45
                   /  \
                 33    72
                      /  \
                     55  84

    Adding 75:
                    45    : RH of RH
                   /  \
                 33    72
                      /  \
                     55  84
                        /
                       75    
     
    rotateLeft(at 45):
                    72
                   /  \
                 45    84
                / \    /
              33  55  75        
    
     */
    XNode* rotateLeft(XNode* root){
        //YOUR CODE HERE
        XNode *newRoot = root->pRight;
        root->pRight = newRoot->pLeft;
        newRoot->pLeft = root;
        root->updateHeight();
        newRoot->updateHeight();
        return newRoot;
    }
    
    /*
    Current tree:
                45
               /  \
             33    72
            /  \
          24    40
    
    Adding 15:
                45    : LH of LH => Rotate right
               /  \
             33    72
            /  \
          24    40
         /
       15     
    rotateRight(at 45):
             33
            /  \
          24    45
         /     /  \
       15     40   72
     *     
     */
    XNode* rotateRight(XNode* root){
        //YOUR CODE HERE
        XNode *newRoot = root->pLeft;
        root->pLeft = newRoot->pRight;
        newRoot->pRight = root;
        root->updateHeight();
        newRoot->updateHeight();
        return newRoot;
    }

    XNode* rebalance(XNode* root){
        //YOUR CODE HERE
        if (root->isEH() ) return root;
        // RIGHT HEAVY
        if (root->isRH() && !root->isBalanced())                   
        {
            // R - R
            if (root->pRight->isRH() || root->pRight->isEH())
                return rotateLeft(root);
            // R - L
            if (root->pRight->isLH())
            {
                root->pRight = rotateRight(root->pRight);
                return rotateLeft(root);
            }
        }
        // LEFT HEAVY
        if (root->isLH() && !root->isBalanced())
        {
            // L - L
            if (root->pLeft->isLH() || root->pLeft->isEH())
                return rotateRight(root);
            // L - R
            if (root->pLeft->isRH())
            {
                root->pLeft = rotateLeft(root->pLeft);
                return rotateRight(root);
            }
        }
        root->updateHeight();
        return root;
    }

    XNode* add(XNode* root, XNode* newNode){
        //YOUR CODE HERE
        if (root == NULL) return newNode;
        if (root->data.key > newNode->data.key)
            root->pLeft = (root->pLeft) ? this->add(root->pLeft, newNode) : newNode;
        else
            root->pRight = (root->pRight) ? this->add(root->pRight, newNode) : newNode;
        root = rebalance(root);
        root->updateHeight();
        return rebalance(root);
    }

    
    XNode* remove(XNode* root, K key, bool& success, V& retValue){
        //YOUR CODE HERE
        root = BST<K,V>::remove(root, key, success, retValue);
        if (!root) return NULL;
        root = rebalance(root);
        root->updateHeight();
        return rebalance(root);
    }
};


#endif /* AVL_H */

