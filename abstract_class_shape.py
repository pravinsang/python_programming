from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    def area(self):
        return self.length * self.breath
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
circle = Circle(1)
rectangle = Rectangle(10, 20)

print(circle.area())
print(rectangle.area())
