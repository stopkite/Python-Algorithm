n = int(input())
sum_val = 0

for _ in range(n):
    a = int(input())
    sum_val += a

avg = sum_val / n

print(f"{sum_val} {avg:.1f}")