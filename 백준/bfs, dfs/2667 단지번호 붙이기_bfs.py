from collections import deque


def solution(n):
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input())))

    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # bfs
    def bfs(graph, a, b):
        cnt = 0
        n = len(graph)

        graph[a][b] = 0
        queue = deque([(a, b)])
        cnt += 1
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
                    cnt += 1

        return cnt

    cnt = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                cnt.append(bfs(graph, i, j))

    cnt.sort()
    print(len(cnt))
    for c in cnt:
        print(c)


n = int(input())
solution(n)
