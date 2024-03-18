# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:59:03 2023

@author: 2367407
@description : Matrix addition
"""

a=[]
b=[]
c=[]
m=int(input("enter the number of rows"))
n=int(input("enter the number of columns"))
print("enter the values in matrix A row wise")
for i in range(0,m):
    a1=[]
    for j in range(0,n):
        a1.append(float(input()))
    a.append(a1)
print("matrix A =",a)        
print("enter the values in matrix B row wise")
for i in range(0,m):
    b1=[]
    for j in range(0,n):
        b1.append(float(input()))
    b.append(b1)
print("matrix B =",a)

sum= []
for i in range(0,m):
    c=[]
    for j in range(0,n):
        c.append(a[i][j]+b[i][j])
    sum.append(c)
    
print("")
print("Addition Matrix :")
print ("")
for i in range(0,m):
    
    for j in range(0,n): 
        print (sum[i][j],end=" ")
    print()
    