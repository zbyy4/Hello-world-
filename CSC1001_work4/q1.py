class Node():
    def __init__(self, element, nxt):
        self.element = element
        self.pointer = nxt

class SinglyLinkedList():
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def enqueue(self, e):
        newest = Node(e, None)
        if self.is_empty():
            self.head = newest
            self.tail = newest
            self.size += 1
        else:
            self.tail.pointer = newest
            self.tail = newest
            self.size += 1
    
    def dequeue(self):
        if self.is_empty():
            print("It's empty!")
        else:
            output = self.head.element
            self.head = self.head.pointer
            self.size -= 1
            if self.is_empty():
                self.tail = None
            return output

    def __str__(self):
        queue = []
        node = self.head
        while node != None:
            queue.append(str(node.element))
            node = node.pointer
        return str(queue)


def countnodes(pointer, numbers=0):
    # test the input
    if type(pointer) != int and type(pointer) != float \
                            and type(pointer) != str:
        if pointer != None:
            numbers += 1
            # use the recursive method
            numbers = countnodes(pointer.pointer, numbers)
        else:
            return numbers
    else:
        return "Inappropriate Input!"

    return numbers


linkedlist = SinglyLinkedList()
for i in range(100):
    linkedlist.enqueue(i)
print("Number of nodes is >", countnodes(linkedlist.head))