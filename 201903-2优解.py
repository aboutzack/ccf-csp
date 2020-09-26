n=input()
for i in range(int(n)):
    exp=input().replace('x','*').replace('/','//')
    if eval(exp)==24:
        print('Yes')
    else:
        print('No')
