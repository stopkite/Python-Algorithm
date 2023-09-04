v = int(input())
e = int(input())

graph = [[] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(v + 1)]


def dfs(x):
    global count
    visited[x] = True
    count += 1
    for node in graph[x]:
        if not visited[node]:
            dfs(node)

count = 0
dfs(1)
print(count - 1)
