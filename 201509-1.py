n=int(input())
l=list(map(int,input().split()))
last=l[0]
count=1
for item in l:
    if item!=last:
        count+=1
    last=item
print(count)
