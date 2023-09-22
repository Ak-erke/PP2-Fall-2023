x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

a=x2-x1
b=y2-y1
if a<0: a=a*-1
if b<0: b=b*-1
if(a==b): print('YES')
else: print('NO')
