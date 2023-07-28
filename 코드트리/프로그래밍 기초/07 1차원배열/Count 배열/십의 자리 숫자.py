cnt_arr = [0] * 10
arr = list(map(int, input().split()))

for elem in arr:
    if elem == 0:
        break
    if elem < 10:
        continue
    cnt_arr[elem // 10] += 1

for i in range(1, 10):
    print(f"{i} - {cnt_arr[i]}")