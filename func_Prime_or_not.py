# Defining a function to check prime or composite
def is_prime(num):
    if num <= 1:
        return "neither Prime nor Composite"
    else:
        for i in range(2, num//2 + 1):
            if num % i == 0:
                return "Composite"
        return "Prime"

# Driver code
num = int(input("Enter a number"))
print(f"{num} is {is_prime(num)}")

        