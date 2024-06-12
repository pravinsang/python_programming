# # square a number using for loop 
# squares = []
# for x in range(1, 6):
#     squares.append(x ** 2)

# print(squares)

# #using list comprehesion
# squares = [ x ** 2 for x in range(1, 6)]
# print(squares)

#selecting even number from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [x for x in numbers if x % 2 == 0]
print(even)