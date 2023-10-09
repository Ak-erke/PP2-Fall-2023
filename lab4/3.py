a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]

x=sorted(set(a)&set(b))
for num in x:
    print(num, end=' ')
