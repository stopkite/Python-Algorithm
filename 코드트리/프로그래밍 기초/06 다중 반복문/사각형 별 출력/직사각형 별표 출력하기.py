arr = input().split()
n, m = int(arr[0]), int(arr[1])

for _ in range(n):
    for _ in range(m):
        print('*', end=" ")
    print()