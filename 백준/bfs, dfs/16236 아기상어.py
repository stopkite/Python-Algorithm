from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dist = [[0] * n for _ in range(n)]

shark_size = 2
cnt_eat = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

cur_x = 0
cur_y = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            cur_x = i
            cur_y = j


def check_size_up():
    global shark_size
    if cnt_eat == 2:
        shark_size += 1


def bfs(tg, i, j):
    global cnt_eat
    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if tg > shark_size:
                continue
            else:
                cnt_eat += 1
                if tg == shark_size:
                    check_size_up()

                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))


for target in range(1, 7):
    if shark_size < target:
        break
    bfs(target, cur_x, cur_y)

max_val = 0
for i in range(n):
    for j in range(n):
        max_val = max(max_val, dist[i][j])

print(max_val)
