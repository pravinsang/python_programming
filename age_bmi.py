age = 47
bmi = 25.5
# if age < 45:
#     if bmi < 22.0:
#         risk = 'low'
#     else: 
#         risk = 'medium'
# else:
#     if bmi < 22.0:
#         risk = 'medium'
#     else:
#         risk = 'high'

young = age < 45
slim = bmi < 22.0

# if young:
#     if slim:
#         risk = 'low'
#     else: 
#         risk = 'medium'
# else:
#     if slim:
#         risk = 'medium'
#     else:
#         risk = 'high'

if young and slim:
    risk = 'low'
elif young and not slim:
    risk = 'medium'
elif not young and slim:
    risk = 'medium'
else:
    risk = 'high'
print(risk)