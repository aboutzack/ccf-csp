n=int(input())
a=[[0 for _ in range(100)] for _ in range(100)]
for i in range(n):
    x1,y1,x2,y2=list(map(int,input().split()))
    for i in range(x1,x2):
        for j in range(y1,y2):
            a[i][j]=1
count=0
for item in a:
    count+=item.count(1)
    #也可count+=sum(item)
print(count)
