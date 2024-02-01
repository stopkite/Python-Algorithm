from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        visited = []
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # b -> a의 방향성을 가진 그래프 추가
        # a라는 수업을 들으려면 b를 먼저 들어야하기 때문
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        # 위상정렬 수행
        q = deque()
        for v in range(numCourses):
            if indegree[v] == 0:
                q.append(v)

        while q:
            cur_v = q.popleft()
            visited.append(cur_v)

            for next_v in graph[cur_v]:
                indegree[next_v] -= 1

                if indegree[next_v] == 0:
                    q.append(next_v)

        if len(visited) == numCourses:
            return True
        else:
            return False


solution = Solution()
print(solution.canFinish(2, [[1, 0]]))  # True
print(solution.canFinish(2, [[1, 0], [0, 1]])) # False
