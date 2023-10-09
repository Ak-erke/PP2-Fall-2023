a=[int(i) for i in input().split()]

number_set=set()

for num in a:
    if num in number_set:
        print('YES')
    else: 
        number_set.add(num)
        print('NO')
