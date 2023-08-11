from collections import deque

answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                q.append((nx, ny))


def count_can_move():
    global answer
    for row in visited:
        for elem in row:
            if elem == True:
                answer += 1


n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    bfs(x - 1, y - 1)

count_can_move()

print(answer)