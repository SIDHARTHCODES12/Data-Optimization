# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:59:03 2023

@author: 2367407 K SIdharth
@description : Vector addition
"""

print("VECTOR ADDITION")
v1=[]
v2=[]
n=int(input("enter the no of elements"))
print("enter the elements in first vector")
for i in range(0,n):
    temp=int(input())
    v1.append(temp)
print("enter the elements in second vector")
for i in range(0,n):
    temp=int(input())
    v2.append(temp)    
vect_sum=[]

for i in range(0,n):
    temp=v1[i]+v2[i]
    vect_sum.append(temp)    
    
print(vect_sum)