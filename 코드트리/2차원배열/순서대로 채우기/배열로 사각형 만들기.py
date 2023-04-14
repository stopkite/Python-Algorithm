arr_2d = [
    [0 for _ in range(5)]
    for _ in range(5)
]

for j in range(5):
    arr_2d[0][j] = 1

for i in range(5):
    arr_2d[i][0] = 1

for i in range(1, 5):
    for j in range(1,5):
        arr_2d[i][j] = arr_2d[i -1][j] + arr_2d[i][j - 1]

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()