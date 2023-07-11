def solution(n, graph):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def dfs(x, y):
        cnt = 1  # 지역 변수로 변경
        graph[x][y] = 0

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                cnt += dfs(nx, ny)  # dfs 호출 결과를 누적

        return cnt

    counts = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                counts.append(dfs(i, j))

    counts.sort()

    print(len(counts))
    for c in counts:
        print(c)


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

solution(n, graph)
