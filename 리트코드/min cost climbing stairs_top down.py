class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        memo = {}

        def dp(n):
            if n == 0 or n == 1:
                return 0

            if n not in memo:
                memo[n] = min(dp(n - 1) + cost[n - 1], dp(n - 2) + cost[n - 2])

            return memo[n]

        return dp(n)


solution = Solution()
solution.minCostClimbingStairs([10, 15, 20])
solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
