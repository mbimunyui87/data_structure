def strassen(matrix1, matrix2):
    # Base case: if matrices are 1x1, perform simple multiplication
    if len(matrix1) == 1:
        return [[matrix1[0][0] * matrix2[0][0]]]

    # Divide matrices into submatrices
    a11, a12, a21, a22 = divide_matrix(matrix1)
    b11, b12, b21, b22 = divide_matrix(matrix2)

    # Compute submatrices products
    p1 = strassen(a11, subtract_matrices(b12, b22))
    p2 = strassen(add_matrices(a11, a12), b22)
    p3 = strassen(add_matrices(a21, a22), b11)
    p4 = strassen(a22, subtract_matrices(b21, b11))
    p5 = strassen(add_matrices(a11, a22), add_matrices(b11, b22))
    p6 = strassen(subtract_matrices(a12, a22), add_matrices(b21, b22))
    p7 = strassen(subtract_matrices(a11, a21), add_matrices(b11, b12))

    # Compute resultant submatrices
    c11 = subtract_matrices(add_matrices(add_matrices(p5, p4), p6), p2)
    c12 = add_matrices(p1, p2)
    c21 = add_matrices(p3, p4)
    c22 = subtract_matrices(subtract_matrices(add_matrices(p5, p1), p3), p7)

    # Combine resultant submatrices
    return combine_matrices(c11, c12, c21, c22)

def divide_matrix(matrix):
    n = len(matrix) // 2
    a11 = [row[:n] for row in matrix[:n]]
    a12 = [row[n:] for row in matrix[:n]]
    a21 = [row[:n] for row in matrix[n:]]
    a22 = [row[n:] for row in matrix[n:]]
    return a11, a12, a21, a22

def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1))] for i in range(len(matrix1))]

def subtract_matrices(matrix1, matrix2):
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1))] for i in range(len(matrix1))]

def combine_matrices(matrix11, matrix12, matrix21, matrix22):
    n = len(matrix11)
    result = [[0] * (2 * n) for _ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix11[i][j]
            result[i][j + n] = matrix12[i][j]
            result[i + n][j] = matrix21[i][j]
            result[i + n][j + n] = matrix22[i][j]
    return result

# Example matrices
matrix1 = [[5, 1], [8, 6]]
matrix2 = [[2, 3], [1, 7]]

# Compute product using Strassen's algorithm
product = strassen(matrix1, matrix2)
print(product)
