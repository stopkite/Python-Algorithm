# B: 벽, M: 폭탄 -> X: 터진 폭탄, E: 빈공간 -> 주위에 폭탄 개수
import copy
from collections import deque


class Solution:
    def updateBoard(self, board, click):
        row_len, col_len = len(board), len(board[0])

        # 대각선 포함 방향이동
        dx = [-1, 1, 1, -1, -1, 1, 0, 0]
        dy = [-1, 1, -1, 1, 0, 0, -1, 1]

        # 폭탄 위치 저장
        bombs = []
        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == 'M':
                    bombs.append((r, c))

        # bfs로 폭탄을 모두 터트려 놓는다.
        revealed_board = copy.deepcopy(board)

        queue = deque()
        for r, c in bombs:
            queue.append((r, c))

        while queue:
            cur_r, cur_c = queue.popleft()

            if revealed_board[cur_r][cur_c] != 'M':
                continue

            for i in range(8):
                next_r = cur_r + dx[i]
                next_c = cur_c + dy[i]
                if next_r < 0 or next_r >= row_len or next_c < 0 or next_c >= col_len:
                    continue

                if revealed_board[next_r][next_c] == 'E':
                    revealed_board[next_r][next_c] = 1
                    queue.append((next_r, next_c))

                elif isinstance(revealed_board[next_r][next_c], int):
                    revealed_board[next_r][next_c] += 1
                    queue.append((next_r, next_c))

        # 폭탄 범위 대각선만 복사해놓는다.
        clicked_r, clicked_c = click[0], click[1]
        for i in range(8):
            next_r = clicked_r + dx[i]
            next_c = clicked_c + dy[i]

            if next_r < 0 or next_r >= row_len or next_c < 0 or next_c >= col_len:
                continue

            board[next_r][next_c] = revealed_board[next_r][next_c]

        # 해당 위치가 터진 폭탄이면 M -> X
        if board[clicked_r][clicked_r] == 'M':
            board[clicked_r][clicked_c] = 'X'
        else:
            board[clicked_r][clicked_c] = 'B'

        print(board)
        print(revealed_board)
        return board


solution = Solution()
solution.updateBoard(
    [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]],
    [3, 0])
# solution.updateBoard(    [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]], [1, 2])
