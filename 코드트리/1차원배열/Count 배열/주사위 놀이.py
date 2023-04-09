cnt_arr = [0] * 7
arr = list(map(int, input().split()))

for elem in arr:
    cnt_arr[elem] += 1

for i in range(1, 7):
    print(f"{i} - {cnt_arr[i]}")