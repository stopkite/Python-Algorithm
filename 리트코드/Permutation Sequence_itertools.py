from itertools import permutations


class Solution:
    def getPermutation(self, n, k):
        result = []
        arr = [i for i in range(1, n + 1)]

        for permutation in permutations(arr, n):
            result.append(list(permutation))

        return ''.join(map(str, result[k - 1]))


solution = Solution()
print(solution.getPermutation(3, 3))
print(solution.getPermutation(4, 9))
print(solution.getPermutation(3, 1))
