def rotate_dir(d):
    nd = d
    rotate = [(0, 3), (3, 2), (2, 1), (1, 0)]
    for i in range(len(rotate)):
        if rotate[i][0] == d:
            nd = rotate[i][1]
    return nd


def rotate_move(nd):
    moves = [(0, (-1, 0)), (3, (1, 0)), (2, (0, 1)), (1, (-1, 0))]  # 서, 남, 동, 북
    for i in range(len(moves)):
        if moves[i][0] == nd:
            return moves[i][1]


n, m = map(int, input().split())
x, y, d = map(int, input().split())

game = []
for _ in range(n):
    data = list(map(int, input().split()))
    for d in data:
        game.append(d)

cnt = 0
answer = 0
while True:
    nd = rotate_dir(d)  # 회전 방향 변경

    move = rotate_move(nd)  # 회전 후 이동
    nx = x + move[0]
    ny = y + move[1]

    if nx < 0 or ny < 0 or nx > m or ny > n:  # 맵 밖으로 빠져나왔을 때
        cnt += 1
        continue
    elif game[nx][ny] == 1:  # 맵이 바다 일 때
        cnt += 1
        continue
    else:
        answer += 1

print(answer)
