n, m = map(int, (input().split()))
A = []
B = []
for i in range(n):
    s = input()
    x, y = map(int, (s.split()[0:2]))
    t = s.split()[2]
    A.append((x,y)) if t == 'A' else B.append((x,y))
for i in range(m):
    l = list(map(int, input().split()))
    result_a = l[0]+l[1]*A[0][0]+l[2]*A[0][1]
    result_b = l[0]+l[1]*B[0][0]+l[2]*B[0][1]
    no = False
    for item in A:
        print(l[0]+l[1]*item[0]+l[2]*item[1], result_a)
        if l[0]+l[1]*item[0]+l[2]*item[1] * result_a<0:
            print('No')
            no = True
            break
    if no:
        continue
    for item in B:
        print(l[0]+l[1]*item[0]+l[2]*item[1], result_b)
        if l[0]+l[1]*item[0]+l[2]*item[1] * result_b<0:
            print('No')
            no = True
            break
    if no:
        continue
    print('Yes')
        
    
