n = int(input())
a = [0, 0, 0, 0]
def skip(num):
    if num % 7 == 0:
        return True
    num = str(num)
    return num.find('7') != -1
count = 0
i = 0
while count<n:
    i += 1
    if skip(i) == False:
        count += 1
    else:
        a[i % 4] += 1
for i in a:
    print(i)
