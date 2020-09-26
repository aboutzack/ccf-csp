n, m = map(int, input().split())
t = 0
k = 0
p = 0
for i in range(n):    
    a = list(map(int, input().split()))
    local_k = 0
    for index, item in enumerate(a):
        t+=item
        if index != 0:
            local_k+=abs(item)
    if local_k>k:
        k = local_k
        p = i
print(t,p+1, k)
    
