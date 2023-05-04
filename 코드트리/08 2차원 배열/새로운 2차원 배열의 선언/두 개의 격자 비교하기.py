n, m = map(int,input().split())
arr_2d = [
    list(map(int, input().split()))
    for _ in range(n * 2)
]


for i in range(n):
    for j in range(m):
        if arr_2d[i][j] == arr_2d[i + n][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()
