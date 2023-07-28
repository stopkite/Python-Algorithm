arr = input().split()
a, b = int(arr[0]), int(arr[1])
sum_val = 0

if b > a:
    for i in range(a, b + 1):
        if i % 5 == 0:
            sum_val += i
else:
    for i in range(b, a + 1):
        if i % 5 == 0:
            sum_val += i


print(sum_val)
