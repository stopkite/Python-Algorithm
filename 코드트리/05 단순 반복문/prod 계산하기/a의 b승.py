arr = input().split()
a, b = int(arr[0]), int(arr[1])
prod = 1

for _ in range(b):
    prod *= a

print(prod)