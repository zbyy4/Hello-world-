class stack:

    def __init__(self):
        self.list = []
        self.topElement = ''

    def push(self,newElement):
        self.list.append(newElement)

    def pop(self):
        try:
            self.topElement = self.list.pop()
            return self.topElement
        except: return None

    def top(self):#return last element of the list
        try:    return self.list[-1]
        except: return -1

    def is_empty(self):
        return len(self.list) == 0

    def __len__(self):
        return len(self.list)

#according to requirements, I only construct one function
def HanoiTower(disks):
    '''swaping method and order:
    odd: A<->C, A<->B, B<->C
    even: A<->B, A<->C, B<->C
    '''
    if disks%2 != 0:    #odd number of tower
        while True:

            if towerA.top() < towerC.top():
                towerA.push(towerC.pop())
                print("C --> A")
            else:
                towerC.push(towerA.pop())
                print("A --> C")
                #helps to test and terminate moving
                if len(towerC) == disks: break

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
                if len(towerC) == disks: break

    else:       #even number of tower
        while len(towerC) != disks:

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
                if len(towerC) == disks: break

            if towerB.top() < towerC.top():
                towerB.push(towerC.pop())
                print("C --> B")
            else:
                towerC.push(towerB.pop())
                print("B --> C")        
                if len(towerC) == disks: break

#construct 3 empty tower
towerA = stack()
towerB = stack()
towerC = stack()

disks = int(input("Number of disks in Tower of Hanoi > "))

#do not change disks number here because it must 
#be ascending order
for i in range(disks):
    towerA.push(i)

HanoiTower(disks)