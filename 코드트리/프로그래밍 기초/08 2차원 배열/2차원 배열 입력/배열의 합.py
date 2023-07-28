arr_2d = []

for _ in range(4):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)

for arr_1d in arr_2d:
    print(sum(arr_1d))