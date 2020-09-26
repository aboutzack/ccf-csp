n=int(input())
is_falled=[0]*(n+1)
falled_count=0
count=0
e=0
for i in range(n):
    l=list(map(int,input().split()))
    now_count=0
    for j in range(1,l[0]+1):
        if l[j]>0:
            if now_count!=l[j] and j!=1:
                #print(now_count,l[j])
                is_falled[i+1]=1
                falled_count+=1
            now_count=l[j]
        else:
            now_count+=l[j]
    count+=now_count

for i in range(1,n+1):
    if i==1:
        if is_falled[n]==is_falled[1]==is_falled[2]==1:
            e+=1
    elif i==n:
        if is_falled[n-1]==is_falled[n]==is_falled[1]==1:
            e+=1
    else:
        if is_falled[i-1]==is_falled[i]==is_falled[i+1]==1:
            e+=1
print(count,falled_count,e)
