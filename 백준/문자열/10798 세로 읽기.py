arr = [[0] * 15 for i in range(5)]
for i in range(5):
    a = list(input())
    for j in range(len(a)):
        arr[i][j] = a[j]
for i in range(15):
    for j in range(5):
        if arr[j][i] == 0:
            continue
        else:
            print(arr[j][i], end='')
