class Flower():
    """ 
    Simulate a flower
    Defult name = Rose , 5 petals, price = 1.0
    """
    def __init__(self, name='Rose', petals_num=5, price=1.0):
        """ initializes variable """
        self.name = name
        if isValid(petals_num, ['Petal','Number']):
            self.petals_num = petals_num
        else:
            self.petals_num = 5
        if isValid(price, ['Price']):
            self.price = price            
        else:
            self.price = 1.0

    def set_name(self, new_name='Rose'):
        self.name = new_name

    def set_petals_num(self, new_petals_num=5):
        if isValid(new_petals_num, ['Petal','Number']):
            self.petalNumber = new_petals_num
        else:
            self.petalNumber = 5

    def set_price(self, new_price):
        if isValid(new_price, ['Price']):
            self.price = new_price
        else:
            self.price = 11

    def get_description(self):
        msg_1 = self.name + " has " + str(self.petals_num) + " petals."
        msg_2 = "The price of it is" + self.price
        print(msg_1)
        print(msg_2)

def isValid(parameter, name):
    # Decide if it is vaild.
    msg = "Invalid input!"
    if type(parameter) == int or type(parameter) == float:
        if parameter > 0:
            return True
        else:
            print(msg)
    else:
        print(msg)
        return False