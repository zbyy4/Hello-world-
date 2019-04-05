import math

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled
    
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
    
    def isfliied(self):
        return self.__filled
    
    def set_filled(self, filled):
        self.__filled = filled
    
    def __str__(self):
        return "color: " + self.__color + \
            " and fiiled: " + str(self.__filled)

class Circle(GeometricObject):
    def __init__(self, radius = 1):
        super().__init__("yellow", True)
        self.__radius = radius

    def get_area(self):
        return self.__radius**2*math.pi
    
    def get_perimeter(self):
        return 2*self.__radius*math.pi

    def print_circle(self):
        print(self.__str__() + " radius: " + str(self.__radius))

c = Circle(1)
print(c.get_area())
print(c)
c.print_circle()