from random import randint

r, y, g = [randint(1, 10) for _ in range(3)]
n = randint(1, 10)
dict = {0: 10, 1:r, 2:y, 3:g}
print(r, y, g)
print(n)
for _ in range(n):
    k = randint(0, 3)
    t = randint(1, dict[k])
    print(k, t)