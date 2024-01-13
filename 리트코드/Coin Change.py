from collections import deque


class Solution:
    def coinChange(self, coins, amount):
        q = deque([(amount, 0)])
        visited = set()
        while q:
            cur, n_coins = q.popleft()
            if cur == 0:
                return n_coins
            for c in coins:
                next = cur - c
                if next not in visited and next >= 0:
                    q.append((next, n_coins + 1))
                    visited.add(next)
        return -1


solution = Solution()
solution.coinChange([1, 2, 5], 11)
# solution.coinChange([2], 3)
# solution.coinChange([1], 0)
# print(solution.coinChange([186, 419, 83, 408], 6249))
