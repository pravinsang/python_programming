# The filter() function in Python takes in a function and an 
# iterable (lists, tuples, and strings) as arguments.
# The function is called with all the items in the list, 
# and a new list is returned, 
# which contains items for which the function evaluates to True.
numbers = [1, 10, 15, 12, 3, 16, 20, 5, 7]

even = list(filter(lambda x : (x % 2 == 0), numbers))
print(even)

double = list(map(lambda x: x * 2, numbers))
print(double)