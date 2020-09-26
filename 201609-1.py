n=int(input())
l=list(map(int,input().split()))
max=abs(l[0]-l[1])
for i in range(n-1):
    a=abs(l[i]-l[i+1])
    if a>max:
        max=a
print(max)
