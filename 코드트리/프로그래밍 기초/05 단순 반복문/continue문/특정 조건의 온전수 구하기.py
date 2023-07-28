# 2로 나누어떨어지지 x
# 일의 자리가 5
# 3으로 나눠 o, 9로 나눠 떨어지지 x
n = int(input())

for i in range(1, n + 1):
    if i % 2 == 0:
        continue

    if i % 10 == 5:
        continue

    if i % 3 == 0 and i % 9 != 0:
        continue

    print(i, end=" ")
