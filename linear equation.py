a=[[1,1,1,2],
   [6,-4,5,31],
   [5,2,2,13]]
n=len(a)
for i in range(n):
    pivot=1/a[i][i]
    for j in range(n+1):
        a[i][j]=pivot*a[i][j]
        for r in range(n):
            if i!=r :
                pivot=a[r][i]
                for j in range(n+1):
                    a[r][j]=a[r][j]-pivot*a[i][j]
                    
for i in range(n):
    print("x",i,"=",int(a[i][n]))