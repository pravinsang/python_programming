start = int(input("Enter the starting value"))
end = int(input("Enter the ending value"))
for num in range(start, end + 1):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")