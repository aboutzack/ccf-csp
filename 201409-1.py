n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(n):
    for j in range(i+1,n):
        if abs(l[i]-l[j])==1:
            count+=1
print(count)
