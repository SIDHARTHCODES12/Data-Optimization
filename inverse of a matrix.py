# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:59:03 2023

@author: 2367407
@description : Finding inverse of a matrix
"""

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
   [1, 2, 3, 4, 5, 1, 0, 0, 0, 0],
   [2, 8, 6, 8, 1, 0, 1, 0, 0, 0],
   [3, 7, 5, 2, 7, 0, 0, 1, 0, 0],
   [4, 1, 2, 7, 2, 0, 0, 0, 1, 0],
   [5, 7, 7, 8, 1, 0, 0, 0, 0, 1]
]
print("Matrix:")
for row in augmented_matrix_AI:
    print(row)
inverse_A = inverse_of_matrix(augmented_matrix_AI)
print("Inverse of A:")
for row in inverse_A:
    print(row)