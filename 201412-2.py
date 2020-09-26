n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(2*n):
    if i<=n-1:
        if i%2==0:
            for j in range(i+1):
                print(l[i-j][j],end=' ')
        else:
            for j in range(i+1):
                print(l[j][i-j],end=' ')
    else:
        c=i-(n-1)
        if i%2==0:
            for j in range(c,i+1-c):
                print(l[i-j][j],end=' ')
        else:
            for j in range(c,i+1-c):
                print(l[j][i-j],end=' ')
