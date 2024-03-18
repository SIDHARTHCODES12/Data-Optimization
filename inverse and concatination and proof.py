# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:27:33 2024

@author: K Sidharth 2367407
         Lab 2a
"""
# creating matrix
a=[[2,3,1],
   [3,3,1],
   [2,4,1]]
b=[[1,-2,3],
   [2,4,5],
   [0,-3,-1]]
print("matrix A :")
print(a)
print("matrix B :")
print(b)
# appendiingmatrix a and b

ab=[]
for i in range (len(a)):
    row=a[i]+b[i]
    ab.append(row)
print("# Concatenate the columns of each row")    
for j in ab:
 print (j)  

#inverse of a matrix

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



# finding the new matrix (s) after making the matrix A as unit matrix from concated AB matrix
print("........................")
print("Matix C")
c = inverse_of_matrix(ab)

 
 #rounding the valus in matrix s 
for i in range (3):
    for j in range(3):
        c[i][j]=round((c[i][j]),2)
for m in c:
 print(m)        
  
  
# matrix multiplication
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
print("........................")


#Multiplying the matrix S and A to get B
temp = matrix_multiplication(a,c)
print("Matrix A x Matrix C")
for z in temp:
 print(z)
 
# checking both matrix are same
if (temp==b):
    print("Hence prooved : Matrix A x Matrix C = Matrix B")
 
