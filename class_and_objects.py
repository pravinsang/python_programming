class Student:

    # Attributes of class
    name = ""
    age = 0

# Creating an instance of class i.e object
stu1 = Student()
stu1.name = "Ram"
stu1.age = 20

stu2 = Student()
stu2.name = "Sita"
stu2.age = 30

print(f"{stu1.name} is {stu1.age} years old")
print(f"{stu2.name} is {stu2.age} years old")

print(type(Student), type(stu1))
print(isinstance(stu1, Student))
print(isinstance(stu1, object))
