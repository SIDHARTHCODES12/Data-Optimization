# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 14:17:14 2024

@author: 2367407 K Sidharth
"""
import numpy as np

def inverse_of_matrix(augmented_matrix):
    n = len(augmented_matrix)
    for k in range(n):
        pivot = augmented_matrix[k][k]
        for j in range(2 * n):
            augmented_matrix[k][j] = augmented_matrix[k][j] / pivot
        for i in range(n):
            if i != k:
                pivot = augmented_matrix[i][k]
                for j in range(2 * n):
                    augmented_matrix[i][j] = augmented_matrix[i][j] - (pivot * augmented_matrix[k][j])
    inverse_matrix = [row[n:] for row in augmented_matrix]
    return inverse_matrix
augmented_matrix_AI = [
   [2, 3, 1, 1, -2, 3],
   [3, 3, 1, 2, 4, 5],
   [2, 4, 1, 0, -3, -1],
   
]
print("A =")
a= [[2, 3, 1],
 [3, 3, 1],
 [2, 4, 1],]
print(a)
print("Matrix:")
for row in augmented_matrix_AI:
    print(row)
inverse_A = inverse_of_matrix(augmented_matrix_AI)
print("Inverse of A:")
for row in inverse_A:
    print(row)
    
print("lastttttttttttt")    
d= np.dot(a,inverse_A)   
print(d)