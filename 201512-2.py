import copy
n,m=list(map(int,input().split()))
a=[]
b=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
    b.append([x for x in l])
for i in range(n):
    for j in range(m):
        count=1
        color=a[i][j]
        for k in range(j+1,m):
            if a[i][k]==color:
                count+=1
            else:
                break
        if count>=3:
            for _ in range(count):
                b[i][j+_]=0

for j in range(m):
    for i in range(n):
        count=1
        color=a[i][j]
        for k in range(i+1,n):
            if a[k][j]==color:
                count+=1
            else:
                break
        if count>=3:
            for _ in range(count):
                b[i+_][j]=0
for i in range(n):
    print(' '.join(map(str,b[i])))
