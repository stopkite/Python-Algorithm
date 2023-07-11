from collections import deque


def solution(n, m, v):
    # 그래프 초기화
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = True
        graph[b][a] = True

    # dfs
    def dfs(start, visited):
        visited[start] = True
        print(start, end=" ")
        for i in range(1, n + 1):
            if not visited[i] and graph[start][i]:
                visited[i] = True
                dfs(i, visited)

    # bfs
    def bfs(start, visited):
        visited[start] = True
        queue = deque([start])
        while queue:
            i = queue.popleft()
            print(i, end=" ")
            for j in range(1, n + 1):
                if not visited[j] and graph[i][j]:
                    visited[j] = True
                    queue.append(j)

    visited = [False] * (n + 1)
    dfs(v, visited)

    print()

    visited = [False] * (n + 1)
    bfs(v, visited)


n, m, v = map(int, input().split())
solution(n, m, v)
