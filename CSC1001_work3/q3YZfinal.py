import random
import time
#fish:river=1:5,bear:fish=1:5
class fish:

    def __init__(self,location=0,river=['N']):
        self.location = location
        self.river = river
        self.step = 0
    
    def generateStep(self):
        if self.location == 0:
            self.step = random.randint(0,1)
        elif self.location == len(self.river)-1:
            self.step = random.randint(-1,0)
        else:
            self.step = random.randint(-1,1)

    def nextMovement(self):
        if self.step == 1:
            self.moveRight()
            return self.location, self.river 
        elif self.step == -1:
            self.moveLeft()
            return self.location, self.river 
        else:
            return self.location, self.river
    
    def vacancySpace(self):
        vacancy = []
        for i in range(len(self.river)):
            if self.river[i] == 'N':
                vacancy.append(i)
        return vacancy
    
    def moveRight(self):
        if self.river[self.location+1] == 'N':
            self.river[self.location], self.river[self.location+1] = self.river[self.location+1], self.river[self.location]
            self.location += 1
        elif self.river[self.location+1] == 'F':
            try:
                vacancy = self.vacancySpace()
                insert = random.randint(0,len(vacancy)-1)
                self.river[vacancy[insert]] = 'F'
            except: pass
        else:
            self.river[self.location] = 'N'
        return self.location, self.river 

    def moveLeft(self):
        if self.river[self.location-1] == 'N':
            self.river[self.location], self.river[self.location-1] = self.river[self.location-1], self.river[self.location]
        elif self.river[self.location-1] == 'F':
            try:
                vacancy = self.vacancySpace()
                insert = random.randint(0,len(vacancy)-1)
                self.river[vacancy[insert]] = 'F'
            except: pass
        else:
            self.river[self.location] = 'N'    
        return self.location, self.river 

class bear:

    def __init__(self,location=0,river=['N']):
        self.location = location
        self.river = river
        self.step = 0
    
    def generateStep(self):
        if self.location == 0:
            self.step = random.randint(0,1)
        elif self.location == len(self.river)-1:
            self.step = random.randint(-1,0)
        else:
            self.step = random.randint(-1,1)

    def nextMovement(self):
        if self.step == 1:
            self.moveRight()
            return self.location, self.river 
        elif self.step == -1:
            self.moveLeft()
            return self.location, self.river 
        else:
            return self.location, self.river
    
    def vacancySpace(self):
        vacancy = []
        for i in range(len(self.river)):
            if self.river[i] == 'N':
                vacancy.append(i)
        return vacancy
    
    def moveRight(self):
        if self.river[self.location+1] == 'N':
            self.river[self.location], self.river[self.location+1] = self.river[self.location+1], self.river[self.location]
            self.location += 1
        elif self.river[self.location+1] == 'B':
            try:
                vacancy = self.vacancySpace()
                insert = random.randint(0,len(vacancy)-1)
                self.river[vacancy[insert]] = 'B'
            except: pass
        else:
            self.river[self.location+1] = 'N'
            self.river[self.location], self.river[self.location+1] = self.river[self.location+1], self.river[self.location]
            self.location += 1
        return self.location, self.river 

    def moveLeft(self):
        if self.river[self.location-1] == 'N':
            self.river[self.location], self.river[self.location-1] = self.river[self.location-1], self.river[self.location]
        elif self.river[self.location-1] == 'B':
            try:
                vacancy = self.vacancySpace()
                insert = random.randint(0,len(vacancy)-1)
                self.river[vacancy[insert]] = 'B'
            except: pass
        else:
            self.river[self.location-1] = 'N'
            self.river[self.location], self.river[self.location-1] = self.river[self.location-1], self.river[self.location]
        return self.location, self.river 

class environment(fish,bear):

    def __init__(self,fishNumber=10,bearNumber=10,riverLength=30,simuTime=10):
        self.fishNumber = fishNumber
        self.bearNumber = bearNumber
        self.riverLength = riverLength
        self.simuTime = simuTime
        self.river = ['F']*fishNumber
        for i in range(bearNumber):
            index = random.randint(0,len(self.river))
            self.river.insert(index, 'B')
        for i in range(riverLength-fishNumber-bearNumber):
            index = random.randint(0,len(self.river))
            self.river.insert(index, 'N')
    
    def simulate(self):
        for i in range(self.simuTime):
            print(''.join(self.river))
            glocation = 0
            while glocation < self.riverLength:
                if self.river[glocation] == 'F':
                    entity = fish(glocation, self.river)
                    entity.generateStep()
                    glocation, self.river = entity.nextMovement()
                elif self.river[glocation] == 'B':
                    entity = bear(glocation, self.river)
                    entity.generateStep()
                    glocation, self.river = entity.nextMovement()               
                glocation += 1
                if 'N' not in self.river and 'F' not in self.river:
                    return None

if __name__ == "__main__":
    e = environment(6,3,80,500)
    e.simulate()