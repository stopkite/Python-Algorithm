arr = input().split()
a, b = int(arr[0]), int(arr[1])
sum_val = 0

for i in range(a, b + 1):
    sum_val += i

print(sum_val)
