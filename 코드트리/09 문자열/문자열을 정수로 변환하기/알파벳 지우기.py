a = input()
b = input()

num1 = ''
for elem in a:
    if elem.isdigit():
        num1 += elem

num2 = ''
for elem in b:
    if elem.isdigit():
        num2 += elem

print(int(num1) + int(num2))