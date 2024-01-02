from itertools import permutations

class Solution:
    def permute(self, nums):
        ans = []
        for permutation in permutations(nums, len(nums)):
            ans.append(list(permutation))
        return ans