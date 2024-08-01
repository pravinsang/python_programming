a = 10
b = int(input("Enter the denominator"))
try:
    result = a / b
    print(result)
except:
    print("Error: denominator cannot be 0.")
