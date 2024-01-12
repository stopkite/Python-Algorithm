from collections import deque


class Solution:
    def isBipartite(self, graph):
        visited = [False] * len(graph)
        colors = [0] * len(graph)

        def bfs(start_v):
            visited[start_v] = True
            queue = deque([start_v])
            colors[start_v] = 1
            while queue:
                cur_v = queue.popleft()
                for next_v in graph[cur_v]:
                    if not visited[next_v]:
                        visited[next_v] = True

                        if colors[next_v] == 0:
                            if colors[cur_v] == 1:
                                colors[next_v] = 2
                            else:
                                colors[next_v] = 1

                        queue.append(next_v)

                    else:
                        if colors[cur_v] == colors[next_v]:
                            return False
            return True

        for i in range(len(graph)):
            if not visited[i] and graph[i]:
                if not bfs(i):
                    return False
        return True


solution = Solution()
print(solution.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(solution.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
print(solution.isBipartite([[1], [0, 3], [3], [1, 2]]))
print(solution.isBipartite(
    [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
     [2, 4, 5, 6, 7, 8]]))
