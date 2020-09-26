n=int(input())
def pri(str):
    if str=='+' or str=='-':
        return 1
    elif str=='x' or str=='/':
        return 2
    else:
        return -1
def cal1(n1,n2,op):
    if op=='+':
        return n1+n2
    elif op=='-':
        return n1-n2
    elif op=='x':
        return n1*n2
    else:
        return n1//n2
def cal(str):
    l_n=[]
    l_o=[]
    i=0
    while i<len(str):
        if str[i].isdigit():
            l_n.append(int(str[i]))
            i+=1
        elif len(l_o)==0:
            l_o.append(str[i])
            i+=1
        elif pri(str[i])<=pri(l_o[-1]):
            n2=l_n.pop()
            n1=l_n.pop()
            op=l_o.pop()
            result=cal1(n1,n2,op)
            l_n.append(result)
        else:
            l_o.append(str[i])
            i+=1
    if l_n[0]==24:
        print('Yes')
    else:
        print('No')
for i in range(n):
    str=input()
    str+='a'
    cal(str)
    
