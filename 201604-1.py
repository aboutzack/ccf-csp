n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(n):
    if i==0 or i==n-1:
        continue
    elif (l[i-1]>l[i] and l[i]<l[i+1]) or (l[i-1]<l[i] and l[i]>l[i+1]):
       count+=1
print(count)
