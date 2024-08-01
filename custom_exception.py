class InvalidAgeException(Exception):
    def __init__(self, message = "Age cannot be less than 18."):
        super().__init__(message)

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAgeException()

except InvalidAgeException as e:
    print(e)