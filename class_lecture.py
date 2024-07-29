# class Book:

#     """Information about a book, including title, list of authors,
#     publisher, ISBN, and price.
#     """

#     def __init__(self, title, authors, publisher, isbn, price):
#         self.title = title
#         self.authors = authors[:]
#         self.publisher = publisher
#         self.ISBN = isbn
#         self.price = price

    
#     def num_authors(self):
#         return len(self.authors)
    
#     def __str__(self):
#         return f'Title: {self.title} Price:{self.price}'

# python_book = Book(
#     'Practical Programming',
#     ['Campbell', 'Gries', 'Montojo'],
#     'Pragmatic Bookshelf',
#     '978-1-6805026-8-8',
#     25.0)

# del python_book

# print(python_book)

# class Student:
#     college_name = "Purwanchal Campus"
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
    
#     def full_name(self):
#         return f'{self.fname} {self.lname}'
    
# s1 = Student("Ram", "Thapa")
# s2 = Student("Sita", "Thapa")
# print(s1.full_name(), Student.college_name)
# print(s2.full_name(), s2.college_name)

class Car:
    def __init__(self, name="", mileage=0.0, color=""):
        self.name = name
        self.mileage = mileage
        self.color = color

    def set_values(self):
        name = input("Enter the name")
        mileage = input("Enter the mileage")
        color = input("Enter the color")
        self.name = name
        self.mileage = mileage
        self.color = color

    def get_values(self):
        return(self.name, self.mileage, self.color)

car_1 = Car("Auto", 25, "Red")
# car_2 = Car()
# car_2.set_values()
name, mileage, color = car_1.get_values()
print(name, mileage, color)
