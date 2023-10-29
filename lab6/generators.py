#task1
'''
def generate_squares(N):
    for i in range(1, N + 1):
        yield i ** 2

N =int(input())
squares_generator = generate_squares(N)

for square in squares_generator:
    print(square)
'''
#task2
'''
def even_numbers_generator(n):
    for number in range(2, n + 1, 2):
        yield number

n = int(input())

even_generator = even_numbers_generator(n)

print(','.join(map(str, even_generator)))
'''
#task3
'''
def divisible_by_3_and_4_generator(n):
    for number in range(0, n + 1):
        if number % 3 == 0 and number % 4 == 0:
            yield number

n = int(input())

for num in divisible_by_3_and_4_generator(n):
    print(num)
    '''
#task4
'''
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input())
b = int(input())

for square in squares(a, b):
    print(square)
'''
#task5
def numbers_from_n_to_0(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())  

for num in numbers_from_n_to_0(n):
    print(num)





