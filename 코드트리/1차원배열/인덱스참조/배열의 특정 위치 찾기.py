arr = list(map(int, input().split()))
sum2 = 0
sum3 = 0
cnt = 0

for i in range(10):
    if (i + 1) % 2 == 0:
        sum2 += arr[i]
    if (i + 1) % 3 == 0:
        sum3 += arr[i]
        cnt += 1

avg3 = sum3 / cnt

print(f"{sum2} {avg3:.1f}")