class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __lt__(self, other):
        return self.width * self.height < other.width * other.height

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

r1 = Rectangle(2, 3)
r2 = Rectangle(3, 4)
r3 = Rectangle(2, 3)
print(r1 < r2)
print(r1 == r2)
print(r1 == r3)