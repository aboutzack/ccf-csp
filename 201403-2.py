n,m=list(map(int,input().split()))
a=[0]
a+=[i for i in range(1,n+1)]
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(m):
    x,y=list(map(int,input().split()))
    for j in range(n,0,-1):
        index=a[j]
        if l[index-1][0]<=x and l[index-1][1]<=y and l[index-1][2]>=x and l[index-1][3]>=y:
            print(index)
            tmp=a[n]
            a[n]=index
            a[j]=tmp
            break
        elif j==1:
            print('IGNORED')
