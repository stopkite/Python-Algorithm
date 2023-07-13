from collections import deque


def solution(n, m, graph):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    answer = graph[n - 1][m - 1]
    return answer


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

print(solution(n, m, graph))
