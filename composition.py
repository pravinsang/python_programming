class Salary: 
	def __init__(self, pay): 
		self.pay = pay 

	def annual_salary(self): 
		return (self.pay*12)

class Employee: 
	def __init__(self, name, age, pay): 
		self.name = name 
		self.age = age 
		self.salary = Salary(pay) # composition 

	def total_sal(self): 
		return self.salary.annual_salary() 

emp = Employee('Ram', 25, 10000) 

print(emp.total_sal()) 
