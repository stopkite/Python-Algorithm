class Solution:
    def twoSum(self, nums, target):
        ans = []

        def backtracking(start):
            if len(ans) == 2:
                if nums[ans[0]] + nums[ans[1]] == target:
                    return True
                else:
                    return False

            for i in range(start, len(nums)):
                ans.append(i)
                backtracking(i + 1)
                ans.pop()

        backtracking(0)