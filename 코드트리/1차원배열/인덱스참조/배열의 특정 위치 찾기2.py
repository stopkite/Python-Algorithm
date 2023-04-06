arr = list(map(int, input().split()))

sum_even = sum(arr[::2])
sum_odd = sum(arr[1::2])

print(abs(sum_even - sum_odd))