# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:59:03 2023

@author: 2367407
@description : Finding rank of a matrix
"""


def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def scale_row(matrix, row, scalar):
    matrix[row] = [element * scalar for element in matrix[row]]

def add_scaled_row(matrix, source_row, target_row, scalar):
    for col in range(len(matrix[source_row])):
        matrix[target_row][col] += scalar * matrix[source_row][col]

def matrix_rank(matrix):
    rows, cols = len(matrix), len(matrix[0])
    rank = 0

    for col in range(cols):
        pivot_row = rank
        while pivot_row < rows and matrix[pivot_row][col] == 0:
            pivot_row += 1
        if pivot_row < rows:
            swap_rows(matrix, rank, pivot_row)
            scale_row(matrix, rank, 1 / matrix[rank][col])
            for row in range(rows):
                if row != rank:
                    add_scaled_row(matrix, rank, row, -matrix[row][col])
            rank += 1

    return rank


matrix = [
    [2, 1, 4, 3],
    [0, 0, 0, 0],
    [0, 3, 0, 2]
]

print("Matrix: ")
for row in matrix:
    print(row)

rank_result = matrix_rank(matrix)
print("Rank of the matrix: ", rank_result)