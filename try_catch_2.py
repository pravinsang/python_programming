a = 10
numbers = [1, 2, 3, 4]
b = int(input("Enter the denominator"))
index = int(input("Enter the index"))
try:
    result = a / b
    print(result)
    data = numbers[index]
    print(data)
except ZeroDivisionError:
    print("Error: denominator cannot be 0.")

except IndexError:
    print("Error: index out of bound.")
