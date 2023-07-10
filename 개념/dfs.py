def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


visited = [False] * 8

graph = [
    [], # 노드의 인덱스가 1부터 시작하기 때문에 비워둔다.
    [2, 6, 7],
    [3, 5],
    [2, 4],
    [3],
    [2],
    [1],
    [1]
]

dfs(graph, 1, visited)