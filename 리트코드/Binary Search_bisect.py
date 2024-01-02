from bisect import bisect_left


class Solution:
    def search(self, nums, target):
        index = bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 9))
