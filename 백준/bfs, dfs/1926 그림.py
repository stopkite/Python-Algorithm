"""
n, m 을 초기화 하는 것에서 실수
paper_size는 bfs가 시작되면 무조건 존재하기 때문에 1로 초기화 해야함
x가 행, y가 열을 의미한다! 헷갈릴만한 요소 !!! 주의!!!
"""
from collections import deque

n, m = map(int, input().split())  # 세로, 가로
papers = [list(map(int, input().split())) for _ in range(n)]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    paper_size = 1
    queue = deque([(i, j)])
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and papers[nx][ny] == 1:
                visited[nx][ny] = True
                paper_size += 1
                queue.append((nx, ny))

    return paper_size


cnt = 0
max_size = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and papers[i][j] == 1:
            max_size = max(max_size, bfs(i, j))
            cnt += 1

print(cnt)
print(max_size)
