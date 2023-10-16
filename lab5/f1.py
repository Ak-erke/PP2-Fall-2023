#functions1
#1
"""
def conv(g):
    ounces=g*28.3495231
    return ounces

a=[int(i) for i in input().split()]
result = [conv(value) for value in a]
print(result)
"""
#2
"""
def convC(f):
    C = (5 / 9)*(f - 32)
    return C

f = [int(i) for i in input().split()]
c = [convC(value) for value in f]
print(c)
"""
#3
"""
def solve(numheads, numlegs):
    for num_ch in range(numheads + 1):
        num_r = numheads - num_ch
        if (2 * num_ch + 4 * num_r) == numlegs:
            return num_ch, num_r
    return None

numh, numl = [int(i) for i in input().split()]
result = solve(numh, numl)
print(result)
"""
#4
"""""
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
"""

#5
""""
def print_permutations(input_string):
    n = len(input_string)
    
    for i in range(n):
        for j in range(i, n):
            
            input_list = list(input_string)
            input_list[i], input_list[j] = input_list[j], input_list[i]
            permuted_string = ''.join(input_list)
            
            print(permuted_string)


input_string = input()
print_permutations(input_string)
"""

#6
"""""
def reverse_words_in_sentence(my_string):
    words = my_string.split()

    reversed_sentence = ""
    for word in reversed(words):
        reversed_sentence += word + " "

    return reversed_sentence.strip()

input_sentence = input()
reversed_result = reverse_words_in_sentence(input_sentence)
print(reversed_result)
"""""
#7
"""""
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

nums=[int(i) for i in input().split()]
print(has_33(nums))
"""""

#8
"""""
def spy_game(nums):
    pos_0 = pos_1 = pos_2 = False

    for num in nums:
        if num == 0 and not pos_0:
            pos_0 = True
        elif num == 0 and pos_0 and not pos_1:
            pos_1 = True
        elif num == 7 and pos_0 and pos_1:
            pos_2 = True

    return pos_0 and pos_1 and pos_2

n=[int(i) for i in input().split()]
print(spy_game(n))
"""""

#9
"""""
def sph_volume(radius):
    if radius > 0:
        volume = (4/3) * 3.14* radius**3
        return volume

r=float(input())
print(sph_volume(r))
"""""

#10
"""""
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list=[int(i) for i in input().split()]
result = unique_elements(my_list)
print(result)
"""""

#11
"""""
def is_palindrome(text):

    text = text.replace(" ", "").lower()

    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

text=input()
print(is_palindrome(text))
"""""
#12
"""""
def histogram(numbers):
    for num in numbers:
        print('*' * num)

numbers=[int(i) for i in input().split()]
histogram(numbers)
"""""

#13
"""""
import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)
    
    guesses = 0
    
    while True:
        try:
            guess = int(input("Take a guess: "))
            guesses += 1
            
            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()
"""""

#14
#Done in this file
