def isValid(parameter, name):
    
    hint = "\nInvalid input, please use func: \
            \n\tset%s(*new %s)\
            \nto input correct %s\n"%(
                ''.join(name),
                ' '.join(name).lower(),
                ' '.join(name).lower()
                )

    if type(parameter) == int or type(parameter) == float:
        if parameter > 0:
            return True
        else:
            print(hint)
    else:
        print(hint)
        return False

class Flower:

    print("\nUser guidance>\
        \n\n\tInitialization> *value = Flower('*flower name',*petal numbers,*price)\
        \n\tDefault value>\
        \n\t\tflower name: Sunflower\
        \n\t\tpetal numbers: 50\
        \n\t\tprice: 11\
        \n\tReminder: please type in number for *petal numbers and *price\
        \n\nValid functions>\
        \n\n\t*value.setName('new name'): reset flower name\
        \n\t*value.setPetalNumber(new petal number): reset petal numbers\
        \n\t*value.setPrice(new price), please type in number: reset price\
        \n\t*value.getName(): print out the name of the flower\
        \n\t*value.getPetalNumber(): print out the petal numbers of the flower\
        \n\t*value.getPrice(): print out the price of the flower\n")

    def __init__(
        self, 
        name = "Sunflower", 
        petalNumber = 50, 
        price = 11):

        self.name = name
        if isValid(petalNumber, ['Petal','Number']):
            self.petalNumber = petalNumber
        else:
            self.petalNumber = 50
        if isValid(price, ['Price']):
            self.price = price            
        else:
            self.price = 11

    def setName(self, newName = "Sunflower"):
        self.name = newName
    
    def setPetalNumber(self, newPetalNumber = 50):
        if isValid(newPetalNumber, ['Petal','Number']):
            self.petalNumber = newPetalNumber
        else:
            self.petalNumber = 50
    
    def setPrice(self, newPrice = 11):
        if isValid(newPrice, ['Price']):
            self.price = newPrice
        else:
            self.price = 11
    
    def getName(self):
        return self.name
    
    def getPetalNumber(self):
        return self.petalNumber

    def getPrice(self):
        return self.price