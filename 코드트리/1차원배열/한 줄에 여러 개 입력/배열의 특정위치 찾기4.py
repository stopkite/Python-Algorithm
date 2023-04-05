arr = list(map(int,input().split()))

sum_val = 0
cnt = 0

for i in range(len(arr)):
    if arr[i] == 0:
        break

    if arr[i] % 2 == 0:
        sum_val += arr[i]
        cnt += 1

print(cnt, sum_val)