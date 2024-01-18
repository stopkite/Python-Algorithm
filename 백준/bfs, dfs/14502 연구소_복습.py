from itertools import combinations
from collections import deque

# 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

row_len, col_len = map(int, input().split())

grid = []
for i in range(row_len):
    grid.append(list(map(int, input().split())))

walls = []
# 벽을 세울 수 있는 경우의 수 담기
for i in range(row_len):
    for j in range(col_len):
        if grid[i][j] == 0:
            walls.append((i, j))


# 빈 칸의 개수 세기
def count_zeros(graph):
    zero_count = 0

    for row in graph:
        zero_count += row.count(0)

    return zero_count


def bfs(r, c, ng, vs):
    queue = deque([(r, c)])
    vs[r][c] = True
    while queue:
        cur_r, cur_c = queue.popleft()
        for i in range(4):
            next_r = cur_r + dx[i]
            next_c = cur_c + dy[i]

            if next_r < 0 or next_r >= row_len or next_c < 0 or next_c >= col_len:
                continue

            if not vs[next_r][next_c] and ng[next_r][next_c] == 0:
                ng[next_r][next_c] = 2
                vs[next_r][next_c] = True
                queue.append((next_r, next_c))


max_values = []
for wall_comb in combinations(walls, 3):
    new_grid = [row[:] for row in grid] ####### 복사 방법 주의
    visited = [[False] * col_len for _ in range(row_len)]
    for i, j in wall_comb:  # 벽 3개 세우기
        new_grid[i][j] = 1

    for r in range(row_len):
        for c in range(col_len):
            if not visited[r][c] and new_grid[r][c] == 2:
                bfs(r, c, new_grid, visited)

    max_value = count_zeros(new_grid)
    max_values.append(max_value)

answer = max(max_values)  # 최대 빈칸 개수 세기
print(answer)
