/*Write a program where:

- struct node: represents a node in linkedlists

- functions createLinkedList:

    + Receive the size of a linked list (>0)
    + create a linked list with value from standard input (stdin) a new node is add to the  END  of the linked list
    + Return a pointer which points to the first node of the linked list.

- Function mergeList:

    + receive 2 head1, head2 pointers of 2 linked lists
    + Function mergeList will change the 1st linked list so that the 2nd linked list will be concatenated to the end of the 1st linked list

- function main reads the linked list's size, calls function createLinkedList to initialize the linked list, then calls function print to print the linked list.

Complete the functions createLinkedList, mergeList

Input:

All the inputs from standard input (stdin) with value in (0; 5000)

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
void mergeList(node* head1, node* head2)
{
    node* ptr = head1;
    while(ptr->next)
    {
        ptr = ptr->next;
    }
    ptr->next = head2;
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
  int m;
  cin>>m;
  node *head1 = createLinkedList(m);
  mergeList(head, head1);
  print(head);
  return 0;
}
