# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:59:03 2023

@author: 2367407 K SIdharth
@description : Finding inner product of two products
"""

a=[]
b=[]
c=0
n=int(input("enter the number of elements"))
print("enter the vector in A")
for i in range(0,n):
    l=float(input())
    a.append(l)
print("vector a =",a)    

print("enter the vector in B")
for i in range(0,n):
     l=float(input())
     b.append(l)  
print("vector b =",b)   
     

for i in range(0,n):
    c+=a[i]*b[i]

print("Inner Product of two vectors A & B =",c)     