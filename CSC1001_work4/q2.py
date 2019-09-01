class Node():
    def __init__(self, element, nxt):
        self.element = element
        self.pointer = nxt

class LinkedList():
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

def quick_sort(head, tail=None):
    '''
    Keep the smaller number in its place
    Move lager number to the back
    '''
    if head == tail:
        return None
    pointer = head.pointer
    key = head

    while pointer != tail:
        if pointer.element < key.element:
            # Put the larger number behind
            if key.pointer.element >= key.element:
                key.element, key.pointer.element = key.pointer.element, key.element
                pointer.element, key.element = key.element, pointer.element
                key = key.pointer
            else:
                pointer.element, key.element = key.element, pointer.element
                key = pointer
        pointer = pointer.pointer    
    
    quick_sort(head, key)
    quick_sort(key.pointer, pointer)
    
    return 

q = LinkedList()
q.enqueue(23)
q.enqueue(45)
q.enqueue(0)
q.enqueue(-2)
q.enqueue(188)
q.enqueue(6)
print("Orginal quene>", q)
quick_sort(q.head)
print("Sorted quene>", q)