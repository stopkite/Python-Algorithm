arr = input().split()
a, b = int(arr[0]), int(arr[1])
max_val = a if a > b else b
print(max_val)