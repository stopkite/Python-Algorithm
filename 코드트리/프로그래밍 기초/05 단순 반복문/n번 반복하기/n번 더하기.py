arr = input().split()
a, n = int(arr[0]), int(arr[1])

for _ in range(n):
    a += n
    print(a)