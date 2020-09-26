n=int(input())
a=[]
b=[0,0,0,0,0]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    score=0
    count=0
    for j in range(n):
        if abs(a[i][0]-a[j][0])==1:
            if abs(a[i][1]-a[j][1])==1:
                score+=1
            if abs(a[i][1]-a[j][1])==0:
                count+=1
        elif abs(a[i][0]-a[j][0])==0:
            if abs(a[i][1]-a[j][1])==1:
                count+=1
    if count==4:
        b[score]+=1
for item in b:
    print(item)
