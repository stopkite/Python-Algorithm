from collections import deque

graph = {
    "A": ["B"],
    "B": ["A", "C", "E"],
    "C": ["B", "D"],
    "D": ["C", "E", "F"],
    "E": ["B", "D", "F"],
    "F": ["D", "E"],
}


def bfs(graph, start_v):
    visited = [start_v]
    q = deque(start_v)
    while q:
        cur_v = q.popleft()

        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                q.append(v)
    return visited


print(bfs(graph, "A"))
