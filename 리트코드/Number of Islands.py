from collections import deque


class Solution:
    def numIslands(self, grid):
        row_len, col_len = len(grid), len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def bfs(r, c):
            queue = deque([(r, c)])
            visited[r][c] = True
            while queue:
                cur_r, cur_c = queue.popleft()
                for i in range(4):
                    next_r = cur_r + dx[i]
                    next_c = cur_c + dy[i]

                    if next_r < 0 or next_r >= row_len or next_c < 0 or next_c >= col_len:
                        continue

                    if not visited[next_r][next_c] and grid[next_r][next_c] == '1':
                        visited[next_r][next_c] = True
                        queue.append((next_r, next_c))
            return

        count = 0
        for i in range(row_len):
            for j in range(col_len):
                if not visited[i][j] and grid[i][j] == '1':
                    bfs(i, j)
                    count += 1

        return count


solution = Solution()
solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
# solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
