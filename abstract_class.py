from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def move(self):
        return "Moving..."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


dog = Dog()
print(dog.speak())  
print(dog.move())  

cat = Cat()
print(cat.speak())  
print(cat.move())   
