class Solution:
    def canVisitAllRooms(self, rooms):
        visited = [False] * len(rooms)

        def dfs(cur_v):
            visited[cur_v] = True
            for next_v in rooms[cur_v]:
                if not visited[next_v]:
                    dfs(next_v)

        dfs(0)
        return all(visited)


solution = Solution()
solution.canVisitAllRooms([[1], [2], [3], []])
