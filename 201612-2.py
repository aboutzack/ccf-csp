t=int(input())
s=0
flag=0
tax1=0
l=[0,3500,5000,8000,12500,38500,58500,83500]
rate=[0,0.03,0.1,0.2,0.25,0.3,0.35,0.45]
#print(len(l),len(rate))
for i in range(8):
    if t>=l[i]:
        flag=i
#print(flag)
for i in range(flag):
    tax1+=(l[i+1]-l[i])*rate[i]
print(tax1)
s=(t+tax1-l[flag]*rate[flag])/(1-rate[flag])
#s=round(s/100)*100
if t<=3500:
    s=t
print(int(s))
