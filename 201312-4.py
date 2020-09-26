n=int(input())
#s=[n+1][6]
s=[[0 for x in range(6)] for y in range(n+1)]
s[1][0]=1
for i in range(2,6):
    s[1][i]=0
for i in range(2,n+1):
    s[i][0]=1
    s[i][1]=s[i-1][0]+s[i-1][1]*2
    s[i][2]=s[i-1][0]+s[i-1][2]
    s[i][3]=s[i-1][1]+s[i-1][2]+s[i-1][3]*2
    s[i][4]=s[i-1][1]+s[i-1][4]*2
    s[i][5]=s[i-1][3]+s[i-1][4]+s[i-1][5]*2
print(s[n][5]%1000000007)


