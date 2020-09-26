r,g,y=list(map(int,input().split()))
n=int(input())
count=0
for i in range(n):
    a,b=list(map(int,input().split()))
    if a==0 or a==1:
        count+=b
    elif a==2:
        count+=b+r
print(count)
