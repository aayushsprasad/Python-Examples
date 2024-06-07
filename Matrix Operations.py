#Matrix Operations
#Name: Aayush Prasad @aprasad
import numpy as np

A = np.array([[1, 2], [3, 4]])  # Example matrix
B = np.array([[5, 6], [7, 8]])  # Example matrix

matrix_sum = A + B
matrix_product = np.dot(A, B)
matrix_inverse = np.linalg.inv(A)

print("Sum of matrices:", matrix_sum)
print("Product of matrices:", matrix_product)
print("Inverse of matrix A:", matrix_inverse)