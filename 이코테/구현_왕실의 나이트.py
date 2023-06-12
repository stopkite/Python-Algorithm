location = input()
x, y = ord(location[0]) - ord('a') + 1, int(location[1])

dx = [-1, 1, -1, 1, -2, -2, 2, 2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]

cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    cnt += 1
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        cnt -= 1

print(cnt)
