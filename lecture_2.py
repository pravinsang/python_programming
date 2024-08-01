# 

# class Salary:
#     def __init__(self, pay):
#         self.pay = pay
#     def annual_salary(self):
#         return self.pay*12
    
# class Employee:
#     def __init__(self, name, age, sal):
#         self.name = name
#         self.age = age
#         self.salary = Salary(sal) # Composition

#     def total_sal(self):
#         return self.salary.annual_salary()

# emp = Employee("Ram", 20, 10000)
# print(emp.name, emp.total_sal())

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
    
#     def full_name(self):
#         return f"{self.fname} {self.lname}"
    
# class Employee(Person):
#     def __init__(self, fname, lname, sal):
#         super().__init__(fname, lname)
#         self.sal = sal
    
#     def full_name(self):
#         return f"Employee Details: {self.fname} {self.lname}"

#     def display_sal(self):
#         return self.sal
    
# class Student(Person):
#     def __init__(self, fname, lname, per):
#         super().__init__(fname, lname)
#         self.per = per

#     def display_per(self):
#         return self.per
    
#     def full_name(self):
#         return f"Student Details: {self.fname} {self.lname}"
    
# emp_1 = Employee("Ram", "Thapa", 50000)
# stu_1 = Student("Hari", "Thapa", 80.5)
# print(f"{emp_1.full_name()} {emp_1.display_sal()}")
# print(f"{stu_1.full_name()} {stu_1.display_per()}")