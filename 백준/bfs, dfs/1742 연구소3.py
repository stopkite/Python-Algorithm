from itertools import combinations
from collections import deque
import copy

answer = 1000000
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 보드 전처리
virus_location = []  # 바이러스 좌표 정보를 담은 배열
for r in range(n):
    for c in range(n):
        if grid[r][c] == 0:
            grid[r][c] = '#'
        elif grid[r][c] == 1:
            grid[r][c] = '-'
        elif grid[r][c] == 2:
            virus_location.append((r, c))
            grid[r][c] = '*'


def bfs(v, new_grid):
    global answer
    queue = deque()
    for r, c in v:
        queue.append([r, c, 0])

    max_level = 0
    while queue:
        cur_r, cur_c, level = queue.popleft()
        for i in range(4):
            next_r = cur_r + dx[i]
            next_c = cur_c + dy[i]

            if next_r < 0 or next_r >= n or next_c < 0 or next_c >= n:
                continue
            next_level = level + 1
            if new_grid[next_r][next_c] == '#':  # 빈칸일 때
                new_grid[next_r][next_c] = next_level
                max_level = max(max_level, next_level)
                queue.append([next_r, next_c, next_level])
            elif new_grid[next_r][next_c] == '*':  # 바이러스 일때
                new_grid[next_r][next_c] = next_level
                queue.append([next_r, next_c, next_level])

    # 모든 칸에 바이러스가 전파되었는지 검사
    for r in range(n):
        for c in range(n):
            if new_grid[r][c] == '#':
                return

    answer = min(answer, max_level)
    return


for virus in combinations(virus_location, m):
    new_grid = copy.deepcopy(grid)
    for r, c in virus:
        new_grid[r][c] = 0  # 활성 바이러스
    bfs(virus, new_grid)

if answer == 1000000:
    answer = -1

print(answer)
