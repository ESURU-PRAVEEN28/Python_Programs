n=int(input())

for i in range(0,2*n-1):
    if(i<n):
        
        for j in range(i,n-1):
            print(" ",end=' ')
        for j in range(0,2*(i)+1):
            if(j==0 or j==2*i):
                print("*",end=' ')
            else:
                print(" ",end=' ')
    else:
        for j in range(n-1,i):
            print(" ",end=' ')
        for j in range(0,2*(2*(n-1)-i)+1):
            if(j==0 or j==2*(2*(n-1)-i)):
                print("*",end=' ')
            else:
                print(" ",end=' ')
    
        
    print()

