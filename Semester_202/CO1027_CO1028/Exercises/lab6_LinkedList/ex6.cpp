/*Write a program where:

- struct node: represents a node in linkedlists

- functions createLinkedList:

    + Receive the size of a linked list (>0)
    + create a linked list with value from standard input (stdin) a new node is add to the  END  of the linked list
    + Return a pointer which points to the first node of the linked list.

- Function insertNode

    + receive the linked list's head pointers, a pointer of a new nodei, the position
    + The function will insert the new node to the input position(head's position is 1). If position <=0, do nothing. If position is greater than the size of the linked list, insert to the end of the linked list.

- function main reads the size of the linked list, calls function createLinkedList to initialize the linked list, then call function print to print the linked list.

Complete functions createLinkedList, insertNode

Input: 

Value from standards input (stdin) with value in (0; 5000)*/

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
node *insertNode(node *head, node *newNode, int position)
{
    node* ptr = head;
    if (position <= 0) return head;
    if (position == 1)
    {
        newNode->next = head;
        return newNode;
    }
    while (position > 2  && ptr->next != NULL)
    {
        position--;
        ptr = ptr->next;
    }
    newNode->next = ptr->next;
    ptr->next = newNode;
    return head;
}
void print(node *head)
{
  while (head != nullptr)
  {
    cout << head->data << endl;
    head = head->next;
  }
}
int main()
{
  int n = 0;
  cin >> n;
  node *head = createLinkedList(n);
  node *newNode = new node();
  cin >> newNode->data;
  int position = 0;
  cin >> position;
  head = insertNode(head, newNode, position);
  print(head);
  return 0;
}


