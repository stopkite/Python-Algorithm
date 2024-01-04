class Solution:
    def partition(self, s):
        ans = []

        def is_palindrome(word):
            return True if word == word[::-1] else False

        def backtracking(start, path):
            if start == len(s):
                ans.append(path[:])
                return

            for i in range(start + 1, len(s) + 1):
                word = s[start: i]
                if is_palindrome(word):
                    path.append(word)
                    backtracking(i, path)
                    path.pop()

        backtracking(0, [])
        return ans


solution = Solution()
print(solution.partition("aab"))
