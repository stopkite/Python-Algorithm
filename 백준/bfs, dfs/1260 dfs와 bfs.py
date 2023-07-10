from collections import deque

n, m, v = map(int, input().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in range(1, n + 1):
        if not visited[i] and graph[start][i]:
            dfs(i)


def bfs(start):
    visited[start] = True
    queue = deque([start])
    while queue:
        V = queue.popleft()
        print(V, end=" ")
        for i in range(1, n + 1):
            if not visited[i] and graph[V][i]:
                visited[i] = True
                queue.append(i)

    return visited


visited = [False] * (n + 1)
dfs(v)

print()

visited = [False] * (n + 1)
bfs(v)
