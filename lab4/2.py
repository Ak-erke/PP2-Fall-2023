a=[int(i) for i in input().split()]
b=[int(i) for i in input().split()]

a1=set(a)
b1=set(b)
cnt=len(a1&b1)
print(cnt)
