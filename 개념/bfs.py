from collections import deque


def bfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for v in graph[v]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
    return visited


visited = [False] * 8

graph = [
    [],  # 노드의 인덱스가 1부터 시작하기 때문에 비워둔다.
    [2, 3, 4],
    [5, 6],
    [1],
    [1],
    [2, 7],
    [2],
    [5]
]

bfs(graph, 1, visited)