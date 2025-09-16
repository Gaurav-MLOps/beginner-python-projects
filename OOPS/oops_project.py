from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__ (self, radius):
        self.radius = radius

    def area(self):
        return 3.12 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, width):
        self.width = width
    
    def area(self):
        return self.width ** 2

class Triangle(Shape):
    def __init__ (self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 1/2 * (self.width * self.height)
    

shapes = [Circle(4), Square(5), Triangle(6, 7)]

for Shape in shapes:
    print(f"{Shape.area()}cm²")  