class Solution:
    def twoSum(self, nums, target):
        nums = [[n, i] for i, n in enumerate(nums)]
        nums.sort(key=lambda x: x[0])
        print(nums)

        l, r = 0, len(nums) - 1

        while l < r:
            num_sum = nums[l][0] + nums[r][0]  # n
            if num_sum == target:
                return [nums[l][1], nums[r][1]]  # i
            elif num_sum > target:
                r -= 1
            else:
                l += 1


solution = Solution()
solution.twoSum([3, 2, 4], 6)
