class Solution:
    def trap(self, height):
        answer = 0
        stack = []
        trapped = height[:]
        pop_element = (0, 0)
        for idx, h in enumerate(height):
            while stack and h >= stack[-1][1]:
                pop_element = stack.pop()
                if stack:
                    left = stack[-1]
                    for j in range(left[0] + 1, idx):
                        trapped[j] = h
                else:
                    left = pop_element
                    for j in range(left[0] + 1, idx):
                        trapped[j] = left[1]
            stack.append((idx, h))

        answer = sum(trapped) - sum(height)
        return answer


solution = Solution()
print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(solution.trap([4, 2, 0, 3, 2, 5]))
