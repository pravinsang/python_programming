students = ["Ram", "Hari", "Shyam"]
grades = [85, 92, 78]

#Searching the grade of hari
index = students.index("Hari")
bob_grade = grades[index]
#print(f"Bob's grade: {bob_grade}")

#using Dictionary
students = {"Ram": 85, "Hari": 92}
students["shyam"] = 78
print(students)
hari_percentage = students["Hari"]
print(f"Hari scored {hari_percentage}")
# cahanging hari percentage.
students["Hari"] = 90
hari_percentage = students["Hari"]
print(f"Hari scored {hari_percentage}")