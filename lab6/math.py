#TASK1 from math import math, tan, pi 

'''
degree = float(input())
radian = degree * (math.pi / 180)
print(radian)
'''
#TASK2
'''
height = float(input())
base1 = float(input())
base2 = float(input())

area = 0.5 * (base1 + base2) * height

print("Area:", area)
'''
#TASK3
'''
sides = int(input())
length = int(input())
area = sides * (length ** 2) / (4 * tan(pi / sides))
print("Area", int(area))
'''
#TASK4
length = int(input())
height = int(input())
area = length*height
print("Area", float(area))