# a = 10
# b = int(input("Enter the value of b: "))
# index = int(input("Enter the value of index: "))
# numbers = [1, 2, 3, 4]

# try:
#     result = a / b
#     print(result)
#     data = numbers[index]
#     print(data)
# except ZeroDivisionError as e:
#     print(e)

# except IndexError:
#     print("Index is out of range")

# class InvalidAgeException(Exception):
#     def __init__(self, message = "Age cannot be less than 18."):
#         super().__init__(message)

# try: 
#     age = int(input("Enter your age: "))
#     if age < 18:
#         raise InvalidAgeException("Age value is less than 18.")
#     else:
#         print("You can vote")

# except InvalidAgeException as e:
#     print(e)

# a = 10
# b = 0
# assert b != 0, "b cannot be zero"
# print(a/b)

import logging

logging.basicConfig(filename="new.log",level = logging.INFO)

def div(a, b):
    try:
        return a / b
    except Exception:
        logging.exception(f"An error occurred with a, b = {a}, {b}") 

a = 20 
b = 0
result = div(a, b)
logging.debug(f"{a}/{b} = {result}")    
