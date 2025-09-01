n=int(input())
for i in range(n):
    for j in range(i,n-1):
        print(" ",end=' ')

    for j in range(i+1):
        print(j+1,end=' ')
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
    
for i in range(n):
    if i==0:
        continue
    for j in range(i):
        print(" ",end=' ')
    for j in range(n-i-1):
        print(j+1,end=' ')
    for j in range(n,i,-1):
        print(j-i,end=' ')
    print()