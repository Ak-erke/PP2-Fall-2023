
#1
import os

def list_directories(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

def list_files(path):
    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

def list_all(path):
    print("\nAll Directories and Files:")
    for entry in os.listdir(path):
        print(entry)

path = r'C:\Users\user\Desktop\optimization'

list_directories(path)

list_files(path)

list_all(path)

# 2 
print('\ntask2')

import os
path = r'C:\Users\user\PP2\lab8\ex2(2).py'

print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))

#3
print('\ntask3')

import os
print("Test a path exists or not:")

path = r'g:\\testpath\\a.txt'
print(os.path.exists(path))

path = r'C:\Users\user\PP2\lab8\ex2(2).py'
print(os.path.exists(path))

#4
print('\ntask4')

path = r'C:\Users\user\PP2\lab8\myfile.txt'

with open(path, 'r', encoding='utf-8') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)

#5
print('\ntask5')

color = ['Blue', 'Green', 'White', 'Purple', 'Pink', 'Yellow']
with open('rainbow.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('rainbow.txt')
print(content.read())

#6
print('\ntask6')

import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"This is file {letter}.txt\n")

#7
print('\ntask7')

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r', encoding='utf-8') as source, open(destination_file, 'w', encoding='utf-8') as destination:
            destination.write(source.read())
        print(f"'{source_file}' successfully copied to '{destination_file}'")
    except FileNotFoundError:
        print(f"Error.")
    except Exception as e:
        print(f"An error: {e}")

source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file(source_file, destination_file)

#8
print('\ntask8')

import os
path = r'C:\Users\user\PP2\lab8\file1.txt'
os.remove(path)







