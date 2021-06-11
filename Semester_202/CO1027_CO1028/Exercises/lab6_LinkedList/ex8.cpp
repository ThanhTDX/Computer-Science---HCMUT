/*Write a program where:

- struct node: represents a node in linkedlists

- functions createLinkedList:

    + Receive the size of a linked list (>0)
    + create a linked list with value from standard input (stdin) a new node is add to the  END  of the linked list
    + Return a pointer which points to the first node of the linked list.

- Function replace:

    + receive the head pointer of the linked list
    + position that needed to be replaced (count from 0)
    + new Value
    + function replace will replace the value at input position to the new Value. If position is equal or greater than the size of the linked list or negative, do nothing.

- Function main reads the linked list's size, calls function createLinkedList to initialize the linked list, then calls function print to print the linked list.

Complete functions createLinkedList, replace

Input:

All the input from standard input (stdin) with value in (0, 5000). Except position can be negative

Output:

Satisfy the requirements*/

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
void replace(node* head, int position, int value)
{
  while(head)
  {
    if (position == 0) 
    {
        head->data = value;
        break;
    }
    else 
    {
        head = head->next;
        position--;
    }
  }
}
void print(node *head)
{
  while (head != nullptr)
  {
    cout << head->data << " ";
    head = head->next;
  }
  cout<<endl;
}
int main()
{
  int n = 0;
  cin >> n;
  node *head = createLinkedList(n);
  print(head);
  int pos, val;
  cin>>pos>>val;
  replace(head, pos, val);
  print(head);
  return 0;
}
