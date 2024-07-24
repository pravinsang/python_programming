class Salary: 
	
	def __init__(self, pay): 
		self.pay = pay 

	def annual_salary(self): 
		return self.pay*12

class Employee: 

	def __init__(self, name, age, sal): 
		self.name = name 
		self.age = age 

		self.salary = sal                       # Aggregation 

	def total_sal(self): 
		return self.salary.annual_salary() 

salary = Salary(10000) 
emp = Employee('Ram', 25, salary) 

print(emp.total_sal()) 
