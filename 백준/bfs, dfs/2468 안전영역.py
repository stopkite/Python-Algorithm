from collections import deque


def solution(n, graph):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    max_num = 0
    for row in graph:
        for elem in row:
            max_num = max(max_num, elem)

    def bfs(a, b, num, visited):
        queue = deque([(a, b)])
        visited[a][b] = True
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if not visited[nx][ny] and graph[nx][ny] > num:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    max_cnt = 0
    for num in range(max_num):
        cnt = 0
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and graph[i][j] > num:
                    bfs(i, j, num, visited)
                    cnt += 1
        max_cnt = max(max_cnt, cnt)

    answer = max_cnt
    return answer


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

print(solution(n, graph))
