# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:59:03 2023

@author: 2367407
@description : solving linear equation
"""

def solution_of_equations(augmented_matrix):
    n = len(augmented_matrix)  
    for k in range(n):
        pivot = augmented_matrix[k][k]
        for j in range(n+1):
            augmented_matrix[k][j] = augmented_matrix[k][j] / pivot
        for i in range(n):
            if i != k:
                pivot = augmented_matrix[i][k]
                for j in range(n+1):
                    augmented_matrix[i][j] = augmented_matrix[i][j] - (pivot * augmented_matrix[k][j])
    return augmented_matrix
matrix = [
    [1.0,  1.0, 1.0,  2.0],
    [6.0, -4.0, 5.0, 31.0],
    [5.0,  2.0, 2.0, 13.0]    
]
print("Matrix:")
for row in matrix:
    print(row)  
result = solution_of_equations(matrix)
print("\nSolution:")
for row in result:
    print(round(row[-1]))