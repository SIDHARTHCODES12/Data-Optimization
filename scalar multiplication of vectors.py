10# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:59:03 2023

@author: 2367407 K SIdharth
@description : Scalar multiplication of vector
"""

a=[]
n=int(input("enter the number of elements in vector :"))
print("enter the element in vector A")
for i in range (0,n):
    l=float(input())
    a.append(l)
    
print("Vector =",a)
b=[]
s=int(input("enter the scalar"))
for i in range(0,n):
  b.append(s*a[i])    

print("Vector =",b)