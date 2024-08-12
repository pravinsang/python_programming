import random

print(random.random())
print(random.uniform(2.1, 5.4))
print(random.randint(2, 10))
print(random.randrange(1, 10, 2))

numbers = [1, 3, 5, 7, 9]
random.shuffle(numbers)
print(numbers)
