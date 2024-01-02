from itertools import combinations


class Solution:
    def subsets(self, nums):
        ans = []
        for r in range(len(nums) + 1):
            for combination in combinations(nums, r):
                ans.append(list(combination))

        return ans


solution = Solution()
print(solution.subsets([1, 2, 3]))
