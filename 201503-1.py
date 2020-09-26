n,m=list(map(int,input().split()))
image=[]
img=[]
for i in range(n):
    l=list(map(int,input().split()))
    image.append(l)
for a in range(m-1,-1,-1):
    for b in range(n):
        print(image[b][a],end=' ')
    print()
