matrix = [
    [1, 5, 8],
    [2, 4, 6],
    [10, 11, 12]
]
print(matrix[0][0])
print(matrix[0])
print(matrix[-1])
print("The matrix is :")
for row in matrix:
    for element in row:
        print(element,end=" ")
    print()