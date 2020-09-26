#每一行总是从左到右坐满,所以只需记住每行还剩多少座位即可,当每行都不满足要求时,从首个空位置坐到最后一个
n=int(input())
l=list(map(int,input().split()))
a=[[0 for i in range(5)] for j in range(20)]
for m in range(n):
    flag0=0
    for i in range(20):
        for j in range(5):
            flag=1
            if 5-j<l[m]:
                break
            for k in range(j,j+l[m]):
                if a[i][k]==1:
                    flag=0
                    break
            if flag==1:
                for k2 in range(l[m]):
                    a[i][j+k2]=1
                    print(i*5+j+k2+1,end=' ')
                flag0=1
                break
        if flag0==1:
            break
    if flag0==1:
        print()
    else:
        for i in range(20):
            for j in range(5):
                if a[i][j]==0:
                    a[i][j]=1
                    print(i*5+j+1,end=' ')
        print()
