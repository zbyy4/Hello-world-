class Stack():
    def __init__(self):
        self.list = []
        self.topElement = ''

    def push(self, newElement):
        self.list.append(newElement)

    def pop(self):
        try:
            self.topElement = self.list.pop()
            return self.topElement
        except:
            return None
    
    def top(self):
        try:
            return self.list[-1]
        except:
            return -1
    
    def is_empty(self):
        return len(self.list) == 0
    
    def __len__(self):
        return len(self.list)

def HanoiTower(disks_num):
    '''
    The compare order depends on the number of disks:
    odd: A--C, A--B, B--C
    even: A--B, A--C, B--C
    ''' 
    if disks_num%2 != 0: 
        while True:
            if towerA.top() < towerC.top():
                towerA.push(towerC.pop())
                print("C --> A")
            else:
                towerC.push(towerA.pop())
                print("A --> C")
                if len(towerC) == disks_num:
                    break
            if towerA.top() < towerB.top():
                towerA.push(towerB.pop())
                print("B --> A")
            else:
                towerB.push(towerA.pop())
                print("A --> B")
            if towerB.top() < towerC.top():
                towerB.push(towerC.pop())
                print("C --> B")
            else:
                towerC.push(towerB.pop())
                print("B --> C")
                if len(towerC) == disks_num:
                    break
    else:
        while True:
            if towerA.top() < towerB.top():
                towerA.push(towerB.pop())
                print("B --> A")
            else:
                towerB.push(towerA.pop())
                print("A --> B")
            if towerA.top() < towerC.top():
                towerA.push(towerC.pop())
                print("C --> A")
            else:
                towerC.push(towerA.pop())
                print("A --> C")
                if len(towerC) == disks_num:
                    break
            if towerB.top() < towerC.top():
                towerB.push(towerC.pop())
                print("C --> B")
            else:
                towerC.push(towerB.pop())
                print("B --> C")        
                if len(towerC) == disks_num:
                    break

# Construst 3 empty tower
towerA = Stack()
towerB = Stack()
towerC = Stack()
disks_num = int(input("Please input the number of disks in Hanoi Tower>"))

for i in range(disks_num):
    towerA.push(i)
HanoiTower(disks_num)