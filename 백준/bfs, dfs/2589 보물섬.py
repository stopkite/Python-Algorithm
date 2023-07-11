import sys
from collections import deque


def solution(graph, h, w):
    # 이동 경로 설정
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # bfs 탐색
    def bfs(x, y):
        visited = [[False] * w for _ in range(h)]
        visited[x][y] = True
        queue = deque([(x, y, 0)])
        max_distance = 0

        while queue:
            x, y, distance = queue.popleft()
            max_distance = max(max_distance, distance)

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if graph[nx][ny] == 'L' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance + 1))

        return max_distance

    # 지도 전범위 탐색
    answer = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 'L':
                max_dist = bfs(i, j)
                answer = max(answer, max_dist)

    print(answer)


h, w = map(int, sys.stdin.readline().split())
graph = []
for _ in range(h):
    graph.append(list(sys.stdin.readline().strip()))

solution(graph, h, w)
