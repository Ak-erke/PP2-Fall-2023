a = int(input())
text = []
for i in range(a):
    for element in input().split():
        text.append(element)
stext=set(text)
print(len(stext))
