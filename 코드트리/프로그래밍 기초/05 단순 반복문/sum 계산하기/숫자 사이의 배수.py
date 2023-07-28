arr = input().split()
a, b = int(arr[0]), int(arr[1])
sum_val = 0
cnt = 0

for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        sum_val += i
        cnt += 1

print(f"{sum_val} {sum_val/cnt:.1f}")