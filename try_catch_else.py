a = 10
b = int(input("Enter the denominator: "))
try:
    result = a / b
except ZeroDivisionError:
    print("Error: denominator cannot be 0.")
else:
    print(result)