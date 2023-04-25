n, m = map(int, input().split())
arr = list(map(int,input().split()))
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            sum_val = arr[i] + arr[j] + arr[k]
            if sum_val > m:
                continue
            else:
                result = max(result, sum_val)

print(result)



