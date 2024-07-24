class Number:
    def __init__(self):
        self.num = None

    def __iter__(self):
        self.num = 1
        return self
    
    def __next__(self):     
        x = self.num
        self.num += 1
        return x
        
n1 = Number()
myiter = iter(n1)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))