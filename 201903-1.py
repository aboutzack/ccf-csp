s=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
max=l[0]
min=l[s-1]
mid=0
if min>max:
    a=min
    min=max
    max=a
if s%2==0:
    result=l[s//2-1]+l[s//2]
    if(result%2==0):
        mid=result//2
    else:
        mid=result/2
else:
    mid=l[int((s-1)/2)]
print(max,mid,min)
