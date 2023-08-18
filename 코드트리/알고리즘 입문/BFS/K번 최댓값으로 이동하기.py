from collections import deque

n, k = map(int, input().split())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]
r, c = map(int, input().split())

visited = [
    [False] * n
    for _ in range(n)
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 이동이 불가능할 경우 stop
# k번 반복
def bfs(x, y):
    cur_r, cur_c = x, y
    max_value = -1

    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1
    while queue:
        if count == k:
            return bfs(x, y)

        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            # 이동 가능 범위 체크
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 방문 조건 체크
            if not visited[nx][ny] and graph[nx][ny] < graph[x][y]:
                if max_value > graph[nx][ny]:
                    continue

                # 최댓값 탐색
                if max_value < graph[nx][ny]:  # 최댓값 갱신
                    max_value = graph[nx][ny]
                elif max_value == graph[nx][ny]:  # 열 번호 비교
                    if nx > cur_r:  # 새로운 열이 더 클 때 값 갱신
                        cur_r, cur_c = nx, ny

                visited[nx][ny] = True
                queue.append((nx, ny))


x, y = r - 1, c - 1
print(bfs(x, y))

