class Solution:
    def isValid(self, s):
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '{':
                stack.append('}')
            elif ch == '[':
                stack.append(']')
            elif stack and stack[-1] == ch:
                stack.pop()
            else:
                return False

        return not stack


solution = Solution()
solution.isValid("()")
solution.isValid("()[]{}")
solution.isValid("(]")
