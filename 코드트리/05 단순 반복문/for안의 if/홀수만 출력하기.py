n = int(input())

for _ in range(1, n + 1):
    k = int(input())
    if k % 2 == 1 and k % 3 == 0:
        print(k)