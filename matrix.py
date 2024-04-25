import numpy as np
import threading

def read_matrix(r, c):
    mat = []
    print("Enter the elements:")
    for i in range(r):
        row = list(map(int, input(f"Enter elements for row {i + 1}: ").split()))
        if len(row) != c:
            print(f"Error: Number of elements in row {i + 1} should be {c}. Please re-enter.")
            return read_matrix(r, c)
        mat.append(row)
    return np.array(mat)

def add_matrices(mat1, mat2):
    return np.add(mat1, mat2)

def multiply_matrices(mat1, mat2):
    return np.matmul(mat1, mat2)

def transpose_matrix(mat):
    return np.transpose(mat)

# Get dimensions of matrices from user input
rows1, cols1 = map(int, input("Enter the number of rows and columns for Matrix 1: ").split())
rows2, cols2 = map(int, input("Enter the number of rows and columns for Matrix 2: ").split())

# Read matrices from user input
print("Matrix 1:")
matrix1 = read_matrix(rows1, cols1)
print("\nMatrix 2:")
matrix2 = read_matrix(rows2, cols2)

# Perform matrix operations using threading
thread_add = threading.Thread(target=add_matrices, args=(matrix1, matrix2))
thread_mul = threading.Thread(target=multiply_matrices, args=(matrix1, matrix2))
thread_transpose = threading.Thread(target=transpose_matrix, args=(matrix1,))

# Start threads
thread_add.start()
thread_mul.start()
thread_transpose.start()

# Wait for threads to finish
thread_add.join()
thread_mul.join()
thread_transpose.join()
