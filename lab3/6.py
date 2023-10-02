a=[int(i) for i in input().split()]
maxi=0
for i in range(0, len(a)):
    if(a[i]>a[maxi]):
        maxi=i

print(a[maxi], maxi)