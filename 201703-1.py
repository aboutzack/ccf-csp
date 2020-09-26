n,k=list(map(int,input().split()))
l=list(map(int,input().split()))
count=0
total=0
i=0
while i<n:
    total=0
    total+=l[i]
    while total<k:
        if i<n-1:
            i+=1
            total+=l[i]
        else:
            break
    count+=1
    i+=1
print(count)
