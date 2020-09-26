n = int(input())
drop = [0 for i in range(n)]
total = 0
for i in range(n):
    l = list(map(int, input().split()))
    local_total = l[1]
    for index, item in enumerate(l):
        if index in [0, 1]:
            continue
        if item<=0:
            local_total += item
        if item>0:
            if local_total>item:
                drop[i] = 1
                local_total = item
    total+=local_total
d = drop.count(1)
e = 0
for index, item in enumerate(drop):
    if item*drop[(index-1)%n]*drop[(index+1)%n] == 1:
        e+=1
print(total, d, e)
        
