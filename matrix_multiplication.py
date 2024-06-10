def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter the value at {i}{j} position"))
            row.append(element)
        matrix.append(row)
    return matrix


def multiply_matrix(matrix_a, matrix_b):
    result = [[ 0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            result[i][j] = 0
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j] 
    
    return result

def display_matrix(matrix, row):
    for row in matrix:
        for element in row:
            print(element,end=" ")
        print()

def main():
    row1 = int(input("Enter the row of matrix A: "))
    col1 = int(input("Enter the col of matrix A: "))
    row2 = int(input("Enter the row of matrix B: "))
    col2 = int(input("Enter the row of matrix B: "))

    if(col1 != row2):
        print("Matrix cannot be multiplied")
        return
    
    matrix_a = input_matrix(row1, col1)
    matrix_b = input_matrix(row2, col2)

    result = multiply_matrix(matrix_a, matrix_b)

    display_matrix(result, row1)

if __name__ == "__main__":
    main()