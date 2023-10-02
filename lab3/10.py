a=[int(i) for i in input().split()]
maxi=0
mini=0
for i in range(1, len(a)):
    if a[i]>a[maxi]: maxi=i
    if a[i]<a[mini]: mini=i
a[mini], a[maxi] = a[maxi], a[mini]
print(' '.join([str(i) for i in a]))
