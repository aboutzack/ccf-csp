n=int(input())
l=list(map(int,input().split()))
l.sort()
min=10000
for i in range(len(l)-1):
    if l[i+1]-l[i]<min:
        min=l[i+1]-l[i]
print(min)
