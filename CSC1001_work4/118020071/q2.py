'''general method: swap element instead of cahnging pointer
'''

class Node:
    def __init__(self,element,nxt):
        self.element = element
        self.pointer = nxt

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.l = []

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self,e):
        newest = Node(e,None)

        if self.is_empty():
            self.head = self.tail = newest
            self.size += 1
        else:
            self.tail.pointer = newest#!!!!key here
            self.tail = newest#!!!key here
            self.size += 1
        self.l.append(newest)
    
    def dequeue(self):
        if self.is_empty():
            print("empty!")
        else:
            output = self.head.element
            self.head = self.head.nxt
            self.size -= 1
            if self.is_empty():
                self.tail = None
            return output

#used to print the sorted linked list out
def printout(start):
    pointer = start
    while pointer != None:
        print(pointer.element)
        pointer = pointer.pointer

#quickSort() move larger number to the back
#and keep smaller number in its place
def quickSort(head, tail=None):
    if head == tail:
        return None
    pointer = head.pointer
    key = head

    while pointer != tail:

        if pointer.element < key.element:
            #put larger number back
            if key.pointer.element >= key.element:  #REALLY IMPORTANT: >=, not just >
                key.element, key.pointer.element = key.pointer.element, key.element
                pointer.element, key.element = key.element, pointer.element
                key = key.pointer
                
            else:
                pointer.element, key.element = key.element, pointer.element
                key = pointer
        pointer = pointer.pointer

    quickSort(head, key)
    quickSort(key.pointer, pointer)
    #return head for printing
    return head


if __name__ == "__main__":
    import random
    #generate a string of numbers
    Q = LinkedQueue()
    for i in range(100):
        Q.enqueue(random.randint(0,100))

    printout(quickSort(Q.head))