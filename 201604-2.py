#从上往下,直到不行
a=[]
b=[]
n=0
for i in range(15):
    l=list(map(int,input().split()))
    a.append(l)
for i in range(4):
    l=list(map(int,input().split()))
    b.append(l)
n=int(input())
#底部有几行是0
count=0
for i in range(3,-1,-1):
    flag=1
    for j in range(4):
        if b[i][j]==1:
            flag=0
            break
    if flag==1:
        count+=1
    else:
        break
b=b[:4-count]
for i in range(12+count):
    flag=1
    for j in range(4-count):
        for k in range(4):
            #print(i,j,k,count)
            if b[j][k]&a[j+i][k+n-1]==1:
                flag=0
                break
        if flag==0:
            break
    if i==11+count:
        #print('ok')
        for j in range(4-count):
            for k in range(4):
                a[i+j][k+n-1]=b[j][k]|a[j+i][k+n-1]
        break
    elif flag==0:
        for j in range(4-count):
            for k in range(4):
                a[i+j-1][k+n-1]=b[j][k]|a[j+i-1][k+n-1]
        break
for i in range(15):
    print(' '.join(map(str,a[i])))
