n=int(input())
l=list(map(int,input().split()))
a=l[:]
for i in range(len(l)):
    if i==0:
        a[i]=(l[i]+l[i+1])//2
    elif i==n-1:
        a[i]=(l[i]+l[i-1])//2
    else:
        a[i]=(l[i-1]+l[i]+l[i+1])//3
for b in a:
    print(b,end=' ')
