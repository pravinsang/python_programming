class Person:  # Parent Class
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        return f"{self.fname} {self.lname}"

class Employee(Person):  # Single Inheritance
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def full_name(self):
        return f"Employee: {self.fname} {self.lname}"

    def display_sal(self):
        return self.salary
    
class Student(Person):  # Hierarchical Inheritance
    def __init__(self, fname, lname, percentage):
        super().__init__(fname, lname)
        self.percentage = percentage

    def full_name(self):
        return f"Student: {self.fname} {self.lname}"

    def display_per(self):
        return self.percentage
    
class Skills:  # Another Parent Class
    def __init__(self, skills):
        self.skills = skills

    def display_skills(self):
        return ", ".join(self.skills)

class WorkingStudent(Person, Skills):  # Multiple Inheritance
    def __init__(self, fname, lname, percentage, skills):
        Person.__init__(self, fname, lname)
        Skills.__init__(self, skills)
        self.percentage = percentage

    def full_name(self):
        return f"Working Student: {self.fname} {self.lname}"
    
class Intern(Employee):  # Multilevel Inheritance
    def __init__(self, fname, lname, salary, duration):
        super().__init__(fname, lname, salary)
        self.duration = duration

    def full_name(self):
        return f"Intern: {self.fname} {self.lname}"

    def display_duration(self):
        return self.duration
    
# Single Inheritance
emp_1 = Employee("Ram", "Thapa", 50000)
print(f"{emp_1.full_name()} with salary {emp_1.display_sal()}")

# Hierarchical Inheritance
stu_1 = Student("Hari", "Thapa", 80.44)
print(f"{stu_1.full_name()} with percentage {stu_1.display_per()}")

# Multiple Inheritance
work_stu = WorkingStudent("Sita", "Shrestha", 75.0, ["Python", "Data Analysis"])
print(f"{work_stu.full_name()} with skills {work_stu.display_skills()} and percentage {work_stu.display_per()}")

# Multilevel Inheritance
intern_1 = Intern("Gita", "Rai", 30000, "6 months")
print(f"{intern_1.full_name()} with salary {intern_1.display_sal()} and duration {intern_1.display_duration()}")