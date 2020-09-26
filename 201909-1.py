row,colum=list(map(int,input().split()))
t=p=0
k=1
for i in range(row):
    l=list(map(int,input().split()))
    n_p=0
    for j in range(colum+1):
        t+=l[j]
        if j!=0:
            n_p+=abs(l[j])
    if n_p>p:
        p=n_p
        k=i+1
print(t,k,p)
