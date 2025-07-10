# program 2: vector matrix operations using numpy
import numpy as np

A = np.array([[9, 5, 3], [4, 5, 6]])
B = np.array([[7, 2, 5], [10, 1, 12]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nAddition:\n", (A + B))
print("Subtraction:\n", (A - B))  
print("Multiplication:\n", (A * B))
print("Division:\n", (A / B))
print("Transpose of A:\n", A.T)
print("Transpose of B:\n", B.T)

print("Dot product:\n", np.dot(A, B.T)) 

