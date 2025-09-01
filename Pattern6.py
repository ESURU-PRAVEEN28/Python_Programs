n=int(input())
for i in range (n-1,-1,-1):
    for j in range (i,-1,-1):
        if j==0 or j==i or i==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
