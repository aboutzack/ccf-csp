n=int(input())
m=int(input())
l=[i for i in range(1,n+1)]
for i in range(m):
    p,q=list(map(int,input().split()))
    for i in range(n):
        if l[i]==p:
            l.pop(i)
            l.insert(i+q,p)
            break
for i in range(n):
    print(l[i],end=' ')
