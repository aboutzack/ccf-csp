n=int(input())
l=list(map(int,input().split()))
count=[0 for _ in range(1001)]
for item in l:
    count[item]+=1
for i in range(1001):
    max=0
    index=0
    for j in range(1001):
        if count[j]>max:
            max=count[j]
            index=j
    if index==0:
        break
    else:
        count[index]=0
    print(index,max)
