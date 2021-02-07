from collections import Counter
a=int(input())
b=list(map(int,input().split()))
c=Counter(b)
d=int(input())
e=0
for i in range(d):
    s,f=input().split()
    
    s=int(s)
    f=int(f)
    if c[s] !=0:
        e=e+f
        c[s]-=1
print(e) 