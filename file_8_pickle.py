import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'{self.name} {self.age}'

person = Person("Alice", 30)

with open('person.pkl', 'wb') as file:
    pickle.dump(person, file)

with open('person.pkl', 'rb') as file:
    person_from_file = pickle.load(file)

print(person_from_file) 
