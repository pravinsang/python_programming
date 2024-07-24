numbers = [2, 10, 11, 8, 7, 3]
largest = numbers[0]
for i in range(1, 6):
    if numbers[i] > largest:
        largest = numbers[i]

print(largest)