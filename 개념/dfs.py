graph = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}

visited = []


def dfs(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)

