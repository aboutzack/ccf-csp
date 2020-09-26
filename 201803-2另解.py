n,L,t = list(map(int,input().split()))
positions=list(map(int,input().split()))
speed = []
for i in range(n):
   speed.append(1)
for j in range(t):
   for k in range(n):
      if positions[k] <= 0 or positions[k] >= L:
         speed[k] = -speed[k]
      for l in range(k+1,n):
         if positions[k] == positions[l]:
            speed[k] = -speed[k]
            speed[l] = -speed[l]
   for m in range(n):
      positions[m] += speed[m]
for o in range(n):
   print(positions[o],end=" ")
