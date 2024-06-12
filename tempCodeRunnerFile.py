a, b = map(int, input("Enter the numbers seperated by space: ").split())

max = lambda a, b: a if a > b else b
print(max(a, b)) 