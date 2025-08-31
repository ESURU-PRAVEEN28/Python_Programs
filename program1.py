n=int(input())
l=[]
for i in range(0,n):
    l.append(int(input()))
k=l

for i in range(n):
    count=0
    for j in range(i+1,n):
        if l[i]==k[j]:
            count+=1
            k[j]=0
    if count>=1 and l[i]!=0:
        print(f"duplicate elements:{l[i]}")
            

