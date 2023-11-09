import re

#with open('row.txt', 'r', encoding='utf-8') as file:
#    data = file.read()

def snake_to_camel_case(snake_text):
    camel = re.split('_+', snake_text)
    camel1 = camel[0] + ''.join(map(lambda x: x.title(), camel[1:]))
    return camel1

test = "Snake_example_"
result = snake_to_camel_case(test)
print(result)
