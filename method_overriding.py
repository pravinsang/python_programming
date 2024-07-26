class Person:               # Parent Class

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def full_name(self):
        return f"{self.fname} {self.lname}"

class Employee(Person):     # Child class
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def full_name(self):
        return f"Employee: {self.fname} {self.lname}"

    def display_sal(self):
        return self.salary
    
class Student(Person):     # Child class
    def __init__(self, fname, lname, percentage):
        super().__init__(fname, lname)
        self.percentage = percentage

    def full_name(self):
        return f"Student: {self.fname} {self.lname}"

    def display_per(self):
        return self.percentage
    

emp_1 = Employee("Ram", "Thapa", 50000)
stu_1 = Student("Hari", "Thapa", 80.44)

print(f"{emp_1.full_name()} {emp_1.display_sal()}")
print(f"{stu_1.full_name()} {stu_1.display_per()}")
