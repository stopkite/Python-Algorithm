class Solution:
    def longestValidParentheses(self, s):
        stack = []
        max_len = 0
        for i, elem in enumerate(s):
            if elem == "(":
                stack.append((i, "("))
            else:
                if stack:
                    if stack[-1][1] == "(":
                        max_len = i - stack.pop()[0] + 1
                else:
                    stack.append((i, ")"))

        answer = max_len
        return answer


solution = Solution()
solution.longestValidParentheses(")()())")
