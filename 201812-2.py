r,y,g=list(map(int,input().split()))
n=int(input())
round=r+y+g
count=0
for i in range(n):
    a,b=list(map(int,input().split()))
    if a==0:
        count+=b
        continue
    real=(count)%round
    if a==1:
        if b-real>=0:
            b=b-real
        elif b+g-real>=0:
            a=3
        elif b+g+y-real>=0:
            a=2
            b=b+g+y-real
        else:
            b=b+g+y+r-real
    elif a==2:
        if b-real>=0:
            b=b-real
        elif b+r-real>=0:
            a=1
            b=b+r-real
        elif b+r+g-real>=0:
            a=3
        else:
            b=b+r+g+y-real
    elif a==3:
        if b-real>=0:
            pass
        elif b+y-real>=0:
            a=2
            b=b+y-real
        elif b+y+r-real>=0:
            a=1
            b=b+y+r-real
        else:
            b=b+y+r+g-real
    if a==1:
        count+=b
    elif a==2:
        count+=b+r
print(count)
