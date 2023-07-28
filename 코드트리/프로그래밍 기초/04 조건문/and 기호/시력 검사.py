left = float(input())
right = float(input())

if left >= 1.0 and right >= 1.0:
    print("High")
elif left >= 0.5 and right >= 0.5:
    print("Middle")
else:
    print("Low")