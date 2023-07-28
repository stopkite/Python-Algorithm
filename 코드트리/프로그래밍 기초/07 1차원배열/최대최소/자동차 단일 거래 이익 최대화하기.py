n = int(input())
arr = list(map(int, input().split()))
max_values = []

for i in range(n):
    for j in range(i+1, n):
        if arr[j] > arr[i]:
            max_values.append(arr[j] - arr[i])

if len(max_values) == 0:
    print("0")
else:
    print(max(max_values))
