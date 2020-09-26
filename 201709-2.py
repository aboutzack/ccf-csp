import copy
n,k=list(map(int,input().split()))
l1=[i for i in range(n+1)]
l2=[]
for i in range(k):
    l3=list(map(int,input().split()))
    l3[2]=l3[1]+l3[2]
    l2.append(l3)
l3=copy.deepcopy(l2)
l2=sorted(l2,key=lambda x:x[0])#钥匙编号排序
l3=sorted(l3,key=lambda x:x[1])#借的时间排序
time=[]
for i in range(k):
    time.append(l2[i][1])
    time.append(l2[i][2])
time=list(set(time))
time.sort()
for i in range(len(time)):
    for j in range(k):
        if l2[j][2]==time[i]:
            index=l1.index(0,1)
            l1[index]=l2[j][0]
    for t in range(k):
        if l3[t][1]==time[i]:
            index=l1.index(l3[t][0])
            l1[index]=0
print(' '.join(map(str,l1))[2:])
