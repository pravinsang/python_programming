# students = {"Ram": 85, "Hari": 92, "Shyam": 80}
# print(students)
# #removing the element of dictionary
# del students["Hari"]
# print(students)
# print("Ram" in students)
# print("Hari" in students)
# #looping over dictionary
# for student in students:
#     print(f"{student} : {students[student]}")

# Dictionary Operations
# scientist_to_birthdate = {'Newton' : 1642, 'Darwin' : 1809,
#                             'Turing' : 1912}
# print(scientist_to_birthdate.keys())
# print(scientist_to_birthdate.values())
# print(scientist_to_birthdate.items())
# print(scientist_to_birthdate.get('Newton'))
# researcher_to_birthdate = {'Curie' : 1867, 'Hopper' : 1906,
#                             'Franklin' : 1920}
# scientist_to_birthdate.update(researcher_to_birthdate)
# print(scientist_to_birthdate)
# researcher_to_birthdate.clear()
# print(researcher_to_birthdate)

scientist_to_birthdate = {'Newton' : 1642, 'Darwin' : 1809,
                            'Turing' : 1912}

for key, value in scientist_to_birthdate.items():
    print(f"{key}: {value}")
