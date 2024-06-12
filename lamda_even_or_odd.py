numbers = list(map(int, input("Enter numbers seperated by space").split()))

is_even = lambda x: "Even" if x % 2 == 0 else "Odd"

for num in numbers:
    print(f"{num} is {is_even(num)}")