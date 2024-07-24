class Student:
    school_name = "Purwanchal Campus"

    def __init__(self, roll, name):
        self.name = name
        self.roll = roll

s1 = Student(1, "Ram")
s2 = Student(2, "Hari")
print(f"{s1.roll}, {s1.name}, {Student.school_name}")
print(f"{s2.roll}, {s2.name}, {Student.school_name}")