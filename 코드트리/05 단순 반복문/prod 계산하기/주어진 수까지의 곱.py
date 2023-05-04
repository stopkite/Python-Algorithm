arr = input().split()
a, b = int(arr[0]), int(arr[1])
prod = 1

for i in range(a, b + 1):
    prod *= i

print(prod)