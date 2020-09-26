n=int(input())
five=n//50
n=n%50
three=n//30
n=n%30
one=n/10
total=five*7+three*4+one
print(int(total))
