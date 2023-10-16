""""
#task1
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input() #Enter a string

    def printString(self):
        print(self.input_string.upper())

stringresult = StringManipulator()
stringresult.getString()
stringresult.printString()

#task2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

length = float(input()) #Enter the length of one side of the square
square = Square(length)
print("Area of the square:", square.area())

#task3
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length = float(input())
width = float(input())

rectangle = Rectangle(length, width)
print("Area of the rectangle:", rectangle.area())

#task4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx ** 2 + dy ** 2)

x1 = float(input())
y1 = float(input())
point1 = Point(x1, y1)

x2 = float(input())
y2 = float(input())
point2 = Point(x2, y2)

point1.show()  
point2.show()  

new_x1 = float(input())
new_y1 = float(input())
point1.move(new_x1, new_y1)

distance = point1.dist(point2)  # Calculate the distance between point1 and point2
print(f"Distance between point1 and point2: {distance}")

#task5
class Account:
    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def deposit(self, plus):

        self.depos = self.balance + plus
        print(self.depos)

    def withdraw(self, minus):

        if(self.balance>=minus):

            self.withdrawal = self.balance - minus
            print(self.withdrawal)
        else:

            print('Insufficient balance')

owner_name = input()
balance_card = float(input())
account = Account(owner_name, balance_card)

print(f"Hello, {owner_name}, you have {balance_card} on your balance, press 1 if you want to deposit or Press 0 if you want to withdraw")
choice = int(input())
if(choice==1):

    add = float(input())
    account.deposit(add)
elif(choice==0):

    substract = float(input())
    account.withdraw(substract)
"""   
#task6
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i*i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

def filter_prime(numbers):
    prime_numbers = []
    i = 0
    while i < len(numbers):
        if is_prime(numbers[i]):
            prime_numbers.append(numbers[i])
        i += 1
    return prime_numbers

numbers = [int(i) for i in input().split()]
result = filter_prime(numbers)
print(result)




