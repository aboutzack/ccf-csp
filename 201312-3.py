n=int(input())
h=list(map(int,input().split()))
a=[]
for i in range(n):
    width=1
    for j in reversed(range(i)):
        if h[j]>=h[i]:
            width+=1
        else:
            break
    for j in range(i+1,n):
        if h[j]>=h[i]:
            width+=1
        else:
            break
    a.append(width*h[i])
print(max(a))
