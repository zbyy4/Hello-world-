Q1:
First it constract a singly linked list.
Then you can use the function "countnodes(pointer, numbers=0)" to count the number of nodes in the list.
In the example I created, the Number of nodes is 100.

Q2:
First it constract a singly linked lisk.
Then you can use the function "quick_sort(head, tail=None)" to sort the list into the ascending order.
(It keep the smaller number in its place and move the lager number behind.)
(It change the elements instead of changing the nodes.)
In the example, I create a list: [23, 45, 0, -2, 188, 6]


Q3:
It first creates three stacks to simulate towerA,B,C.
For different number of disks, the comparation order is different.
(odd: A--C, A--B, B--C; even: A--B, A--C, B--C)
Input the number of disks, then they will be put on tower A.
Move the disks until TowerC is full.
For every steps, it will print out the detial. (From where --> to where)