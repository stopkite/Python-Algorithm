arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        idx = i
        break

sum_val = 0
for i in range(idx - 3, idx):
    sum_val += arr[i]

print(sum_val)

# print(arr[idx - 3] + arr[idx - 2] + arr[idx - 1])

