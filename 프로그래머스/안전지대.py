def solution(board):
    cnt = 0
    steps = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    n = len(board)

    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                for dx, dy in steps:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] != 1:
                            board[nx][ny] = 2

    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                cnt += 1

    return cnt


solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])
