import re

with open('row.txt', 'r', encoding='utf-8') as file:
    data = file.read()

#task1
matches = re.findall(r'a[b]*', data)
print(matches)

print()#task2

pattern1 = r'ab{2,3}'
matches1 = re.findall(pattern1, data)
print(matches1)

print()#task3

pattern2 = r'[a-z]+_[a-z]+'
matches2 = re.findall(pattern2, data)
print(matches2)

print()#task4

pattern3 = r'[A-Z][a-z]+'
matches3 = re.findall(pattern3, data)
print(matches3)

print()#task5

pattern4 = r'a.*b'
matches4 = re.findall(pattern4, data)
print(matches4)

print()#task6

pattern5 = r'[ ,.]'
result = re.sub(pattern5, ':', data)
print(result)

print()#task7

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return ''.join(x.capitalize() for x in components)

camel_case_string = snake_to_camel(data)
print(camel_case_string)

print()#task8

pattern7 = r'[A-Z]'
splits = re.split(pattern7, data)
print(splits)
#for split in splits:
#    print(split)

print()#task9

pattern8 = r'(?<=[a-z])(?=[A-Z])'
result = re.sub(pattern8, ' ', data)
print(result)

print()#task10

def camel_to_snake(camel_str):
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_str).lower()

snake_case_string = camel_to_snake(data)
print(snake_case_string)