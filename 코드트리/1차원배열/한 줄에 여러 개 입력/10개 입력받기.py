arr = list(map(int, input().split()))

sum_val = 0
cnt = 0
for i in range(len(arr)):
    if arr[i] == 0:
        break
    cnt += 1
    sum_val += arr[i]

avg_val = sum_val / cnt

print(f"{sum_val} {avg_val:.1f}")
