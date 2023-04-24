a, b = input().split()

num1 = ''
for elem in a:
    if elem.isdigit() == False:
        break
    else:
        num1 += elem

num2 = ''
for elem in b:
    if elem.isdigit() == False:
        break
    else:
        num2 += elem

print(int(num1) + int(num2))