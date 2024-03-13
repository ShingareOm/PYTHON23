# Write a Python program to create two matrices and perform addition, subtraction,
# multiplication and division operation on matrix.


def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input("Enter element at position ({}, {}): ".format(i + 1, j + 1)))
            row.append(element)
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        print(row)

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

def multiply_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

def divide_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] / matrix2[i][j])
        result.append(row)
    return result

# Example usage:
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter elements of first matrix:")
matrix1 = create_matrix(rows, cols)

print("Enter elements of second matrix:")
matrix2 = create_matrix(rows, cols)

print("\nFirst matrix:")
display_matrix(matrix1)

print("\nSecond matrix:")
display_matrix(matrix2)

print("\nAddition:")
addition_result = add_matrices(matrix1, matrix2)
display_matrix(addition_result)

print("\nSubtraction:")
subtraction_result = subtract_matrices(matrix1, matrix2)
display_matrix(subtraction_result)

print("\nMultiplication:")
multiplication_result = multiply_matrices(matrix1, matrix2)
display_matrix(multiplication_result)

print("\nDivision:")
division_result = divide_matrices(matrix1, matrix2)
display_matrix(division_result)
