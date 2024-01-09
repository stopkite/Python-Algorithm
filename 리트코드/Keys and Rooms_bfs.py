from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms):
        visited = [False] * len(rooms)

        queue = deque([0])
        while queue:
            cur_v = queue.popleft()
            visited[cur_v] = True
            for v in rooms[cur_v]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)

        return all(visited)


solution = Solution()
# solution.canVisitAllRooms([[1],[2],[3],[]])
solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
