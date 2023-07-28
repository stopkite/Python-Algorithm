n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def get_num_of_coin(row_s, row_e, col_s, col_e):
    num_of_coin = 0

    for row in range(row_s, row_e + 1):
        for col in range(col_s, col_e + 1):
            if grid[row][col] == 1:
                num_of_coin += 1

    return num_of_coin


max_coin = 0
for row in range(n):
    for col in range(n):
        if col + 2 >= n or row + 2 >= n:
            continue

        num_of_coin = get_num_of_coin(row, row + 2, col, col + 2)
        max_coin = max(num_of_coin, max_coin)

print(max_coin)
