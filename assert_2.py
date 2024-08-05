def calculate_average(numbers):
    assert len(numbers) > 0, "List is Empty"
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
print(calculate_average(numbers))

