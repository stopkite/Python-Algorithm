import heapq


class Solution:
    def networkDelayTime(self, times, n: int, k: int):
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((w, v))

        pq = []
        costs = {}
        heapq.heappush(pq, (0, k))
        while pq:
            cur_cost, cur_v = heapq.heappop(pq)
            if cur_v not in costs:
                costs[cur_v] = cur_cost
                for cost, next_v in graph[cur_v]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_v))

        if len(costs) == n:
            return max(costs.values())
        else:
            return -1


solution = Solution()
print(solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
print(solution.networkDelayTime([[1, 2, 1]], 2, 1))
print(solution.networkDelayTime([[1, 2, 1]], 2, 2))
