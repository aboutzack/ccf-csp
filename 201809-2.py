n=int(input())
h=[]
w=[]
count=0
for i in range(n):
    h.append(list(map(int,input().split())))
for i in range(n,2*n):
    w.append(list(map(int,input().split())))
start=0
for i in range(n):
    h_l=h[i]
    flag=0
    for j in range(start,n):
        w_l=w[j]
        if h_l[0]<=w_l[0] and h_l[1]>=w_l[0]:
            if h_l[1]>w_l[1]:
                count+=w_l[1]-w_l[0]
            else:
                count+=h_l[1]-w_l[0]
            #print(h_l[1]-w_l[0],h_l,w_l)
            if flag==0:
                start=j
                flag=1
        elif w_l[0]<=h_l[0] and w_l[1]>=h_l[0]:
            if w_l[1]>h_l[1]:
                count+=h_l[1]-h_l[0]
            else:
                count+=w_l[1]-h_l[0]
            #print(w_l[1]-h_l[0],h_l,w_l)
            if flag==0:
                start=j
                flag=1
        elif flag==1:
            break
        #print(start)
print(count)
