class CustomException(Exception):
    def __init__(self, message = "Value cannot be negative"):
        super().__init__(message)

a = int(input("Enter a number"))
try:
    if a < 0:
        raise CustomException("a cannot be negative")
    print("A is positive")
    
except CustomException as e:
    print(e)