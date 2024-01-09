graph = {
    "A": ["B"],
    "B": ["A", "C", "E"],
    "C": ["B", "D"],
    "D": ["C", "E", "F"],
    "E": ["B", "D", "F"],
    "F": ["D", "E"],
}

visited = []


def dfs(cur_v):
    visited.append(cur_v)
    for next_v in graph[cur_v]:
        if next_v not in visited:
            dfs(next_v)


dfs("A")

print(visited)
