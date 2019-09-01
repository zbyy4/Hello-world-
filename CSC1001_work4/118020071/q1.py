class Node:
    def __init__(self,element,nxt):
        self.element = element
        self.pointer = nxt

class SinglyLinkedList:
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
            self.tail.pointer = newest
            self.tail = newest
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


def nodesNumber(pointer, numbers=0):
    #test the inappropriate imput
    if type(pointer) != int and type(pointer) != float and type(pointer) != str: 

        if pointer != None:
            numbers += 1
            #recursion counting method
            numbers = nodesNumber(pointer.pointer, numbers)
        else:
            return numbers
    
    else:
        return "Your input is not inappropriate"

    return numbers


if __name__ == "__main__":
    Q = SinglyLinkedList()
    for i in range(100):
        Q.enqueue(i)

    print(nodesNumber(Q.head))

