n=int(input())
l=list(map(int,input().split()))
a={}
for i in l:
    a[i]=l.count(i)
a=sorted(a.items(),key=lambda x:(-x[1],x[0]))
for x,y in a:
    print(x,y)
