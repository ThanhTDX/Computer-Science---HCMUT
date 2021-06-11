/*Write a program where:

- struct node: represents a node in linkedlists

- functions createLinkedList:

    + Receive the size of a linked list (>0)
    + create a linked list with value from standard input (stdin) a new node is add to the  First  position of the linked list
    + Return a pointer which points to the first node of the linked list.

- Function main reads the size of the linked list, calls function createLinkedList to Initialize the linked list, then call function print to print the linked list.

Complete function createLinkedList

Input:

size n of the linked list (0 < n < 5000)

following by n numbers, each number is a value of a node in the linked list, each number is an integer in (-5000; 5000)

Output:

Satisfy the requirements*/

#include <iostream>
#include <vector>
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
void print(node *head)
{
    vector<int> vec;
    while (head != nullptr)
    {
        vec.push_back(head->data);
        head = head->next;
    }
    for (int i = (int)vec.size() - 1; i >= 0; i--)
    {
        std::cout << vec[i] << endl;
    }
}
int main()
{
  int n = 0;
  cin >> n;
  if (n > 0)
  {
    node *head = createLinkedList(n);
    print(head);
  }
  else
  {
    cout << "Invalid n" << endl;
  }
  return 0;
}