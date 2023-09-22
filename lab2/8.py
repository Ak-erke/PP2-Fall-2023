x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())

if x2==x1 or x2==x1-1 or x2==x1+1:
    if y2==y1 or y2==y1-1 or y2==y1+1:
        print ('YES')
    else: print('NO')
else: print('NO')
