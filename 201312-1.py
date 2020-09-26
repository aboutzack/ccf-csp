n=int(input())
l=list(map(int,input().split()))
a=[0]*10001
for i in range(n):
    a[l[i]]+=1
max=0
max_index=0
for i in range(1,10001):
    if a[i]>max:
        max=a[i]
        max_index=i
print(max_index)
