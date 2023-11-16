# 1
'''
from functools import reduce

numbers = input()
numbers = [float(num) for num in numbers.split()]
result = reduce(lambda x, y: x * y, numbers)
print(result)

# 2
text = input()
upper = 0
lower = 0

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print("upper case:", upper)
print("lower case:", lower)

# 3
string = input()
string = string.replace(" ", "").lower()
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# 4
import math
import time

number = float(input())
milliseconds = int(input())
time.sleep(milliseconds / 1000) 
result = math.sqrt(number)
print(result)
'''
# 5
elements = (1, True, True)
result = all(elements)
if result:
    print("All elements are True.")
else:
    print("Not all elements are True.")
