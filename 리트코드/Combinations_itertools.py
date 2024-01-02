from itertools import combinations


class Solution:
    def combine(self, n, k):
        ans = []
        nums = [i for i in range(1, n + 1)]

        combines = combinations(nums, k)
        for combine in combines:
            ans.append(combine)

        return ans
