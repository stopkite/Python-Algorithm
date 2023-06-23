def solution(keyinput, board):
    n, m = board[0], board[1]
    up_limit = -(m // 2)
    down_limit = m // 2

    left_limit = -(n // 2)
    right_limit = n // 2

    x, y = 0, 0
    for k in keyinput:
        if k == "left" and x - 1 >= left_limit:
            x -= 1
        elif k == "right" and x + 1 <= right_limit:
            x += 1
        elif k == "down" and y - 1 >= up_limit:
            y -= 1
        elif k == "up" and y + 1 <= down_limit:
            y += 1

    answer = [x, y]

    return answer
