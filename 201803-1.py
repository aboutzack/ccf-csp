l=list(map(int,input().split()))
total=0
count=0
for i in range(len(l)):
    if l[i]==1:
        total+=1
        count=0
    elif l[i]==2:
        count+=1
        total+=count*2
print(total)
