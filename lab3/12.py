a=[int(i) for i in input().split()]
k, C = [int(i) for i in input().split()]

a.append(C)
for i in range(len(a)-1, k, -1):
    a[i], a[i-1] = a[i-1], a[i]
    
print(' '.join([str(i) for i in a]))
