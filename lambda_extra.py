# lamda with list comprehension

func_list = [lambda arg=x: arg for x in range(5)]

for func in func_list:
    print(func())

# lambda with if..else
a, b = map(int, input("Enter the numbers seperated by space: ").split())

max = lambda a, b: a if a > b else b
print(max(a, b)) 
