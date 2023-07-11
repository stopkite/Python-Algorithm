from collections import deque

def solution(n, m):
    cnt = 0

    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = True
        graph[b][a] = True

    visited = [False] * (n + 1)

    visited[1] = True
    queue = deque([1])
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in range(1, n + 1):
            if not visited[i] and graph[v][i]:
                visited[i] = True
                queue.append(i)

    answer = cnt - 1
    print(answer)


n = int(input())
m = int(input())
solution(n, m)
