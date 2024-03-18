# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:22:29 2024

@author: 2367407 K Sidharth
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:06:36 2024

@author: Nelson
"""

a=[[1,-3,-26,22,7],[1,0,-8,7,6],[1,1,-2,2,0],[4,5,-2,3,0],[1,-3,-26,22,0]]
print("Matrix A")
for row in a:
 print(row)    
#row=int(input("Enter the no of rows: "))
#col=int(input("Enter the no of rows: "))
#a=take(a,row,col)
#print("Matrix a: ",a)
#b=take(b,row,col)
#print("Matrix b: ",b)
for ind in range(5):
    if(a[ind][ind]==0):
        for ind4 in range(ind+1,5):
            if(a[ind4][ind4]!=0):
                a[ind],a[ind4]=a[ind4],a[ind]
                break
    else:
        p=a[ind][ind]
        for ind1 in range(5):
            a[ind][ind1]=round(a[ind][ind1]/p,2)
        for ind1 in range(5):
            if(ind1!=ind):
                pivot=a[ind1][ind]
                for ind2 in range(5):
                    a[ind1][ind2]=a[ind1][ind2]-((a[ind][ind2])*pivot)

count=0
for ind in range(5):
    if(a[ind][ind]!=0):
        count+=1
print("Matrix After Row Operation")
print(".............................")
for row in a:
 print(row)   
print("...........................")     
print("Rank: ",count)