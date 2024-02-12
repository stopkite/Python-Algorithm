class Solution:
    def twoSum(self, nums, target):
        memo = {}
        for i, num in enumerate(nums):
            needed = target - num
            if needed in memo:
                return [memo[needed], i]
            memo[num] = i



solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3], 6))
