n = int(input())
count = 0
num = 0
ans = [0, 0, 0, 0]
while count<n:
    num+=1
    if num %7 == 0 or '7' in str(num):
        ans[num%4-1] += 1
    else:
        count+=1
for i in ans:
    print(i)
    
