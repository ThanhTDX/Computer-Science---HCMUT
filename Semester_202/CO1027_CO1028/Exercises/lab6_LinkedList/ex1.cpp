/*Write a program where:

- struct node: represents a node in linkedlists

- functions createLinkedList:

    + Receive the size of a linked list (>0)
    + create a linked list with value from standard input (stdin) a new node is add to the  END  of the linked list
    + Return a pointer which points to the first node of the linked list.

- Function isEqual compare two linked list:

   + Receive the pointer head1 of the 1st linked list , pointer head2 of the 2nd linked list

   + Return true if and only if 2 the linked lists have indentical size, and node value. Otherwise, return false.


- Function main reads the size of the linked list, calls function createLinkedList to Initialize the linked list, then call functdion print to print all the node's values of the linked list.

Complete function createLinkedList, isEqual 

Input: 

The value input from standard input (stdin) with value in (0; 5000)*/

#include <iostream>
using namespace std;
struct node
{
  int data;
  node *next;
  node() : data{0}, next{NULL} {};
  node(int data, node* next) : data{data}, next{next}{};
};
node *createLinkedList(int n)
{        
    int value;
    std::cin >> value;
    node* head = new node(value, NULL);
    node* ptr = head;
    for (int i = 1; i < n; i++)
    {
        std::cin >> value;
        node* newNode = new node(value, NULL);
        ptr->next = newNode;
        ptr = ptr->next;
    }
    return head;
}
bool isEqual(node *head1, node *head2)
{
    node *ptr1 = head1, *ptr2 = head2;
    while(ptr1 && ptr2)
    {
        if (ptr1->data != ptr2->data) return false;
        if (ptr1->next == NULL && ptr2->next == NULL) return true;
        else 
        {
            ptr1 = ptr1->next;
            ptr2 = ptr2->next;
        }
    }
    return false;
}
int main()
{
  int n = 0;
  cin>> n;
  node *head1 = createLinkedList(n);
  int m = 0;
  cin>> m;
  node *head2 = createLinkedList(m);
  cout << isEqual(head1, head2) << endl;
  return 0;
}
