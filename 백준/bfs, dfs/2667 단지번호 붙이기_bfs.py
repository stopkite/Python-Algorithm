from collections import deque


def solution(n, graph):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs(x, y):
        cnt = 0
        n = len(graph)

        graph[x][y] = 0
        cnt += 1
        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
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
                cnt.append(bfs(i, j))

    cnt.sort()

    print(len(cnt))
    for c in cnt:
        print(c)


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

solution(n, graph)
