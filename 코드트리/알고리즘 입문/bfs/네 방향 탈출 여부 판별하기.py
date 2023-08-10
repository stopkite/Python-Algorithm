from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque([(0, 0)])
    visited[0][0] = True
    while q:
        cur_x, cur_y = q.popleft()

        for i in range(4):
            nx = dx[i] + cur_x
            ny = dy[i] + cur_y

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] != 0 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

bfs()
answer = 1 if visited[n - 1][m - 1] else 0
print(answer)