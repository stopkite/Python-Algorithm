arr_1d = [
    list(map(int, input().split()))
    for _ in range(3)
]

input()

arr_2d = [
    list(map(int, input().split()))
    for _ in range(3)
]

arr_3d = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arr_3d[i][j] = arr_1d[i][j] * arr_2d[i][j]

for row in arr_3d:
    for elem in row:
        print(elem, end=" ")
    print()
