from itertools import product

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr_p = []
for k in range(len(str(n))):
    for i in product(arr, repeat=k+1):
        arr_p.append(i)

numbers = []
for row in arr_p:
    res = ''
    for elem in row:
        res += str(elem)
    numbers.append(int(res))

numbers.sort()

max_val = 0
for number in numbers:
    if n >= number:
        max_val = max(max_val, number)
    else:
        break

print(max_val)
