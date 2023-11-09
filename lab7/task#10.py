import re

#with open('row.txt', 'r', encoding='utf-8') as file:
#    data = file.read()

def camel_to_snake_case(camel_str):
    snake_str = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_str)
    return snake_str.lower()

mycamelstring = "ConvertCamelCaseStringToSnakeCase"
snakecasestring = camel_to_snake_case(mycamelstring)

print(snakecasestring)
