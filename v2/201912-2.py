n = int(input())
ans = [0, 0, 0, 0, 0]
dic = dict()
l = list()
for i in range(n):
    a = tuple(map(int, input().split()))
    dic[a] = 1
    l.append(a)
for i in range(n):
    score=0
    x = l[i][0]
    y = l[i][1]
    if (x, y+1) in dic and (x, y-1) in dic\
       and (x-1, y) in dic and (x+1, y) in dic:
        if (x+1,y+1) in dic:
            score+=1
        if (x+1,y-1) in dic:
            score+=1
        if (x-1,y+1) in dic:
            score+=1
        if (x-1,y-1) in dic:
            score+=1
        ans[score]+=1
for i in ans:
    print(i)
