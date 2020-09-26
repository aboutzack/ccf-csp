n=int(input())
l=list(map(int,input().split()))
a=[0]*1001
for i in range(n):
    a[l[i]]+=1
    print(a[l[i]],end=' ')
    
