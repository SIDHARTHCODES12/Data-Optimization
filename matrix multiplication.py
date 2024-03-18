# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:56:49 2023

@author: 2367410

@description: Ex2: Multiplication of two matrices
"""


def get_matrix():
    matrix_str = input("Enter a matrix(rows separated by semicolons and columns separated by commas): ")
    matrix = [[float(value) for value in row.split(',')] for row in matrix_str.split(';')]
    print(matrix)
    return matrix


def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for performing matrix multiplication")
    result_matrix = []
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix2[0])):
            dot_product = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0])))
            row_result.append(dot_product)
        result_matrix.append(row_result)
    return result_matrix
    
    
matrix1 = get_matrix()
matrix2 = get_matrix()

result = matrix_multiplication(matrix1, matrix2)
print("Result of matrix multiplication = ", result)
