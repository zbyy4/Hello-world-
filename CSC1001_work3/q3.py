import random
import time


class Fish():
    """ Simulate the fish"""
    def __init__(self, location, living_river):
        """ Basic fish state """
        self.location = location           # the index in the river
        self.living_river = living_river   # the whole river
        self.move_decision = 0             # the decision of next step         
    
    def generate_step(self):
        """ Randomly decide where to move or stay """
        if self.location == 0:
            self.move_decision = random.randint(0,1)
        elif self.location == len(self.living_river)-1:
            self.move_decision = random.randint(-1,0)
        else:
            self.move_decision = random.randint(-1,1)

    def next_movement(self):
        """ Make the next move """
        if self.move_decision == 1:
            self.move_right()
            return self.location, self.living_river 
        elif self.move_decision == -1:
            self.move_left()
            return self.location, self.living_river 
        else:
            return self.location, self.living_river
    
    def vacancy_space(self):
        vacancy = []
        for i in range(len(self.living_river)):
            if self.living_river[i] == 'N':
                vacancy.append(i)
        return vacancy
    
    def move_right(self):
        """ Judgement for fish to move right """
        if self.living_river[self.location+1] == 'N':
            self.living_river[self.location], self.living_river[self.location+1] = self.living_river[self.location+1], self.living_river[self.location]
            self.location += 1
        elif self.living_river[self.location+1] == 'F':
            try:
                vacancy = self.vacancy_space()
                insert = random.randint(0,len(vacancy)-1)
                self.living_river[vacancy[insert]] = 'F'
            except: pass
        else:
            self.living_river[self.location] = 'N'
        return self.location, self.living_river 

    def move_left(self):
        """ Judgement for fish to move left """
        if self.living_river[self.location-1] == 'N':
            self.living_river[self.location], self.living_river[self.location-1] = self.living_river[self.location-1], self.living_river[self.location]
        elif self.living_river[self.location-1] == 'F':
            try:
                vacancy = self.vacancy_space()
                insert = random.randint(0,len(vacancy)-1)
                self.living_river[vacancy[insert]] = 'F'
            except: pass
        else:
            self.living_river[self.location] = 'N'    
        return self.location, self.living_river 

class Bear():
    """ Simulate the Bear"""
    def __init__(self, location, living_river):
        """ Basic bear state """
        self.location = location           # the index in the river
        self.living_river = living_river   # the whole river
        self.move_decision = 0             # the decision of next step
    
    def generate_step(self):
        """ Randomly decide where to move or stay """
        if self.location == 0:
            self.move_decision = random.randint(0,1)
        elif self.location == len(self.living_river)-1:
            self.move_decision = random.randint(-1,0)
        else:
            self.move_decision = random.randint(-1,1)

    def next_movement(self):
        """ Make the next move """
        if self.move_decision == 1:
            self.move_right()
            return self.location, self.living_river 
        elif self.move_decision == -1:
            self.move_left()
            return self.location, self.living_river 
        else:
            return self.location, self.living_river
    
    def vacancy_space(self):
        vacancy = []
        for i in range(len(self.living_river)):
            if self.living_river[i] == 'N':
                vacancy.append(i)
        return vacancy
    
    def move_right(self):
        """ Judgement for bear to move right """
        if self.living_river[self.location+1] == 'N':
            self.living_river[self.location], self.living_river[self.location+1] = self.living_river[self.location+1], self.living_river[self.location]
            self.location += 1
        elif self.living_river[self.location+1] == 'B':
            try:
                vacancy = self.vacancy_space()
                insert = random.randint(0,len(vacancy)-1)
                self.living_river[vacancy[insert]] = 'B'
            except: pass
        else:
            self.living_river[self.location+1] = 'N'
            self.living_river[self.location], self.living_river[self.location+1] = self.living_river[self.location+1], self.living_river[self.location]
            self.location += 1
        return self.location, self.living_river 

    def move_left(self):
        """ Judgement for bear to move left """
        if self.living_river[self.location-1] == 'N':
            self.living_river[self.location], self.living_river[self.location-1] = self.living_river[self.location-1], self.living_river[self.location]
        elif self.living_river[self.location-1] == 'B':
            try:
                vacancy = self.vacancy_space()
                insert = random.randint(0,len(vacancy)-1)
                self.living_river[vacancy[insert]] = 'B'
            except: pass
        else:
            self.living_river[self.location-1] = 'N'
            self.living_river[self.location], self.living_river[self.location-1] = self.living_river[self.location-1], self.living_river[self.location]
        return self.location, self.living_river 

class Environment():
    """ Simulate the whole river """
    def __init__(self, fish_number=8, bear_number=4, river_length=140, simu_time=800):
        """ Creat the river, is a list """
        self.fish_number = fish_number
        self.bear_number = bear_number
        self.river_length = river_length
        self.simu_time = simu_time
        self.living_river = ['F']*fish_number
        for i in range(bear_number):
            index = random.randint(0,len(self.living_river))
            self.living_river.insert(index, 'B')
        for i in range(river_length-fish_number-bear_number):
            index = random.randint(0,len(self.living_river))
            self.living_river.insert(index, 'N')
    
    def simulate(self):
        for i in range(self.simu_time):
            print(''.join(self.living_river))
            glocation = 0
            while glocation < self.river_length:
                if self.living_river[glocation] == 'F':
                    entity = Fish(glocation, self.living_river)
                    entity.generate_step()
                    glocation, self.living_river = entity.next_movement()
                elif self.living_river[glocation] == 'B':
                    entity = Bear(glocation, self.living_river)
                    entity.generate_step()
                    glocation, self.living_river = entity.next_movement()               
                glocation += 1
                # If there is no fish or empty space, the process will stop.
                if 'N' not in self.living_river and 'F' not in self.living_river:
                    return None

if __name__ == "__main__":
    # Defult 8 fished, 4 bears, river lengh is 140, simulate 800 times
    e = Environment(8,4,140,800)
    e.simulate()
