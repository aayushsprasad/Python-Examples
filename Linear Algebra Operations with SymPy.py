#Linear Algebra Operations with SymPy
#Name: Aayush Prasad @aprasad
import numpy as np
from sympy import symbols, Matrix

# Define symbols
x, y, z = symbols('x y z')

# Define matrices
A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
B = Matrix([[2, 3, 4], [1, 0, -1], [2, 5, 3]])

# Perform operations
sum_matrices = A + B
product_matrices = A * B
inverse_matrix_A = A.inv()

# Print results
print("Sum of matrices:", sum_matrices)
print("Product of matrices:", product_matrices)
print("Inverse of matrix A:", inverse_matrix_A)