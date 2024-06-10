#square the numbers of a list
numbers = [2, 4, 6, 8, 10, 12]
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2

print("Final Numbers are: ")
print(numbers)