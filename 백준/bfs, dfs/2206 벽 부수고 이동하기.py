from collections import deque


def solution(n, m, graph):
    start_x = 0
    start_y = 0

    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(start_x, start_y, 1)])
    visited[start_x][start_y][1] = 1
    while queue:
        x, y, wall = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                visited[nx][ny][wall] = visited[x][y][wall] + 1
                queue.append((nx, ny, wall))
            elif graph[nx][ny] == 1 and wall == 1:
                visited[nx][ny][0] = visited[x][y][wall] + 1
                queue.append((nx, ny, 0))

    return -1


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

print(solution(n, m, graph))
