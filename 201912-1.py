n=int(input())
count=0
i=0
a=[0,0,0,0]
def func(a):
    a=str(a)
    return a.find('7')!=-1
while count<n:
    i+=1
    if i%7==0 or func(i):
        a[i%4-1]+=1
    else:
        count+=1
for i in a:
    print(i)
