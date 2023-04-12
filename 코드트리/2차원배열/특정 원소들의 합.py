arr_2d = []

for _ in range(4):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)

sum_val = 0
for i in range(4):
    for j in range(i + 1):
        sum_val += arr_2d[i][j]

print(sum_val)
