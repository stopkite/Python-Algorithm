cnt = 0

while True:
    n = int(input())

    if n % 2 == 1:
        continue

    print(n // 2)
    cnt += 1

    if cnt >= 3:
        break