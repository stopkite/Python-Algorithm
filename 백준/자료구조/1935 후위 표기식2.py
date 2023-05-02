n = int(input())
example = list(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

temp = []
for i in example:
    if 'A' <= i <= 'Z':
        idx = ord(i) - ord('A')
        temp.append(numbers[idx])
    else:
        b = temp.pop()
        a = temp.pop()

        if i == '+':
            temp.append(a + b)
        elif i == '-':
            temp.append(a - b)
        elif i == '*':
            temp.append(a * b)
        elif i == '/':
            temp.append(a / b)

print(f"{temp[0]:.2f}")
