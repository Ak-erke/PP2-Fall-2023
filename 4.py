n = int(input())
n=n%(24*60)

a=n//60
b=n-a*60
print(a, b)
