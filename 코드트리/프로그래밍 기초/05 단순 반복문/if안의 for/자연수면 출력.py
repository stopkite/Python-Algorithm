arr = input().split()
a, b = int(arr[0]), int(arr[1])

if a > 0:
    for _ in range(b):
        print(a, end="")
else:
    print(0)