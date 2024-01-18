from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        visited = [[False] * n for _ in range(n)]

        dx = [-1, 1, 1, -1, -1, 1, 0, 0]
        dy = [-1, 1, -1, 1, 0, 0, -1, 1]

        if grid[0][0] == 1:
            return -1

        queue = deque([(0, 0, 1)])
        visited[0][0] = True
        while queue:
            cur_r, cur_c, cur_distance = queue.popleft()

            if cur_r == n - 1 and cur_c == n - 1:
                return cur_distance

            for i in range(8):
                next_r = dx[i] + cur_r
                next_c = dy[i] + cur_c

                if next_r < 0 or next_r >= n or next_c < 0 or next_c >= n:
                    continue

                if not visited[next_r][next_c] and grid[next_r][next_c] == 0:
                    visited[next_r][next_c] = True
                    queue.append((next_r, next_c, cur_distance + 1))

        return -1


solution = Solution()
s1 = solution.shortestPathBinaryMatrix([[0, 1], [1, 0]])
s2 = solution.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]])
s3 = solution.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]])

print(s1) # 2
print(s2) # 4
print(s3) # -1
