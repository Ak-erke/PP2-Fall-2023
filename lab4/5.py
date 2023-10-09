al, bl=[int(i) for i in input().split()]

anya, borya=set(), set()

for i in range(al):
    anya.add(int(input()))
for i in range(bl):
    borya.add(int(input()))

print(len(set(anya&borya)))

for num in anya&borya:
    print(num, end=' ')
print()

print(len(set(anya-borya)))

for num in sorted(anya-borya):
    print(num, end=' ')
print()

print(len(set(borya-anya)))
for num in sorted(borya-anya):
    print(num, end=' ')