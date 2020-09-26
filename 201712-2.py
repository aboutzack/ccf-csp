n,k=list(map(int,input().split()))
l=[i for i in range(1,n+1)]
count=0
while len(l)>1:
    poped=0
    for i in range(len(l)):
        count+=1
        if (count%k==0 or count%10==k) :
            l.pop(i-poped)
            poped+=1
        if len(l)==1:
            break
print(l[0])
