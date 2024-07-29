class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)
    
p1 = Point(3, 8)
p2 = Point(2, 4)
p3 = p1 + p2
p4 = p1 - p2
print(p3)
print(type(p4))

# a = 10 
# b = 20
# c = a.__add__(b)
# print(c)
