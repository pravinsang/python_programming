# 
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @property
#     @abstractmethod
#     def area(self):
#         pass


# class Rectangle(Shape):
#     def __init__(self, length, breath):
#         self.length = length
#         self.breath = breath

#     @property
#     def area(self):
#         return self.length * self.breath
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     @property
#     def area(self):
#         return 3.14 * self.radius ** 2

    
# r1 = Rectangle(10, 20)
# c1 = Circle(1)
# print(r1.area)

# a = 10
# b = 20
# print(a.__add__(b)) # a + b

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)
    
#     def __sub__(self, other):
#         x = self.x - other.x
#         y = self.y - other.y
#         return Point(x, y)
    
#     def __str__(self):
#         return f"({self.x},{self.y})"
    
# p1 = Point(2, 3)
# p2 = Point(4, 5)
# print(p1 + p2)          #p1.__add__(p2)
# print(p1 - p2)          #p1.__sub__(p2)

