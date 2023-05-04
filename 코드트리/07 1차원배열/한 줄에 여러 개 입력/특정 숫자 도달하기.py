arr = list(map(int, input().split()))
sum_val = 0
cnt = 0

for elem in arr:
    if elem >= 250:
        break
    cnt += 1
    sum_val += elem

avg = sum_val / cnt

print(f"{sum_val} {avg:.1f}")
