n = int(input())
temp = []

if n ** 0.5 % 1 == 0:
    temp.append(1)
else:
    for i in range(1, int((n // 2) ** 0.5) + 1):
        for j in range(1, int((n - i ** 2) ** 0.5) + 1):
            if i ** 2 + j ** 2 == n:
                temp.append(2)
            elif (n - i ** 2 - j ** 2) ** 0.5 % 1 == 0:
                temp.append(3)
            else:
                temp.append(4)

ans = min(temp)
print(ans)
