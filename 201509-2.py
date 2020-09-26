def func(a):
    if a%400==0 or (a%4==0 and a%100!=0):
        return True
y=int(input())
d=int(input())
l=[31,28,31,30,31,30,31,31,30,31,30,31]
if func(y):
    l[1]+=1
i=0
while True:
    if d-l[i]>0:
        d-=l[i]
        i+=1
    else:
        break
print(i+1)
print(d)
