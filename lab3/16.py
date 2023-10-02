rr = [0]*9
cc = [0]*9
xx = [0]*16
zz = [0]*16
res = False
for i in range(8):
    r,c = map(int,input().split())
    x = r-c+8
    z = r+c-8
    if (rr[r] + cc[c] + xx[x] + zz[z]) != 0:
        res = True
    else:
        rr[r] = 1
        cc[c] = 1
        xx[x] = 1
        zz[z] = 1
        
if res:
    print('YES')
else:
    print('NO')
