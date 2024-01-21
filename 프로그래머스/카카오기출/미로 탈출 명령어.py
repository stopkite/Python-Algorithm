from collections import deque


def solution(n, m, x, y, r, c, k):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    grid = [['.'] * m for _ in range(n)]
    grid[x - 1][y - 1] = 'S'
    grid[r - 1][c - 1] = 'E'

    moved = []
    queue = deque([(x - 1, y - 1, "")])
    while queue:
        cur_r, cur_c, cur_move = queue.popleft()

        if len(cur_move) == k and cur_r == r - 1 and cur_c == c - 1:
            moved.append(cur_move)

        if len(cur_move) > k and cur_r == r - 1 and cur_c == c - 1:
            break

        for i in range(4):
            next_r = cur_r + dx[i]
            next_c = cur_c + dy[i]

            if next_r < 0 or next_r >= n or next_c < 0 or next_c >= m:
                continue

            next_move = cur_move

            if dx[i] == -1 and dy[i] == 0:
                next_move += "l"
            elif dx[i] == 1 and dy[i] == 0:
                next_move += "r"
            elif dx[i] == 0 and dy[i] == -1:
                next_move += "u"
            elif dx[i] == 0 and dy[i] == 1:
                next_move += "d"

            grid[next_r][next_c] = next_move
            queue.append((next_r, next_c, next_move))

    moved.sort()

    if not moved:
        answer = "impossible"
    else:
        answer = moved[0]

    return answer


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(2, 2, 1, 1, 2, 2, 2))
print(solution(3, 3, 1, 2, 3, 3, 4))
