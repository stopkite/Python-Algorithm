n, m = map(int, input().split())
x, y, dir = map(int, input().split())

game = []
for _ in range(n):
    data = list(map(int, input().split()))
    game.append(data)

game[x][y] = 1  # 처음 위치 방문 처리

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]


def turn_left(dir):
    dir -= 1
    if dir == -1:
        dir = 3
    return dir


answer = 1
cnt = 0
while True:
    # 왼쪽으로 회전
    dir = turn_left(dir)
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 회전 후 이동한 곳이 처음일 때
    if game[nx][ny] == 0:
        game[nx][ny] = 1
        x = nx
        y = ny
        answer += 1
        cnt = 0
        continue
    else:  # 회전 후 이동한 곳이 바다인 경우
        cnt += 1

    if cnt == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if game[nx][ny] == 0:
            x = nx
            y = ny
            answer += 1
        else:  # 뒤가 바다면
            break
        cnt = 0

print(answer)
