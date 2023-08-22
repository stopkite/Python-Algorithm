n, m = map(int, input().split())

martix = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

visited = [False for _ in range(n + 1)]

count = 0
def dfs(v):
    global count
    for cur_v in range(1, n + 1):
        if martix[v][cur_v] and not visited[cur_v]:
            count += 1
            visited[cur_v] = True
            dfs(cur_v)

for _ in range(m):
    a, b = map(int, input().split())
    martix[a][b] = 1
    martix[b][a] = 1

visited[1] = True
dfs(1)
print(count)
