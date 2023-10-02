a=[int(i) for i in input().split()]
cnt=1
for i in range(0, len(a)-1):
    if a[i]!=a[i+1]:
        cnt+=1
    
print(cnt)