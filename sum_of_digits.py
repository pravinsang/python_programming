num = int(input("Enter a number"))
sum_of_digits = 0
while num != 0:
    rem = num % 10
    sum_of_digits = sum_of_digits + rem
    num = num // 10

print(f"Sum of digits = {sum_of_digits}")