n=int(input())
l=list(map(int,input().split()))
l.sort()
number=-1
for i in range(n):
    a=l[i]
    j=i
    while j>=0 and a==l[j]:
        j-=1
    k=i
    while k<n and a==l[k]:
        k+=1
    if j+1==n-k:
        number=a
print(number)
