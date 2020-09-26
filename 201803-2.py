n,l,t=list(map(int,input().split()))
a=list(map(int,input().split()))
b=sorted(a)
seq=[]
for i in range(n):
    for j in range(n):
        if a[i]==b[j]:
            seq.insert(i,j)
a=b
a.insert(0,0)
a.insert(len(a),l)
d=['r']*n
d.insert(0,'r')
d.insert(len(a),'l')
#print(a)
#print(d)
for i in range(t):
    for j in range(1,n+1):
        if d[j]=='r':
            a[j]+=1
        else:
            a[j]-=1
    for j in range(1,n+1):
        if d[j]=='l' and d[j-1]=='r' and a[j]==a[j-1]:
            d[j]='r'
            if j!=1:
                d[j-1]='l'
        elif d[j]=='r' and d[j+1]=='l' and a[j]==a[j+1]:
            d[j]='l'
            if j!=n:
                d[j+1]='r'
for i in range(n):
    print(a[seq[i]+1], end=' ')
