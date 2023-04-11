arr = list(map(int, input().split()))
max_val = arr[0]
min_val = arr[0]

for elem in arr:
    if elem == 999 or elem == -999:
        break

    if elem < min_val:
        min_val = elem

    if elem > max_val:
        max_val = elem

print(max_val, min_val)