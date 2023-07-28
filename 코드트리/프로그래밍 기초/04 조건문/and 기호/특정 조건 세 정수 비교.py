arr = input().split()
a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

minimum = min(a, b, c)

print(1 if a == minimum else 0, end=" ")
print(1 if a == b and b == c else 0)