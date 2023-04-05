n = int(input())
score = list(map(float,input().split()))

sum_val = sum(score)
avg_val = sum_val / n

print(f"{avg_val:.1f}")

if avg_val >= 4.0:
    print("Perfect")
elif avg_val >= 3.0:
    print("Good")
else:
    print("Poor")