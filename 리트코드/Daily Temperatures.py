class Solution:
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []
        for day, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                pre_day = stack.pop()[0]
                ans[pre_day] = day - pre_day
            stack.append((day, temp))
        return ans


solution = Solution()
solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print("--------")
solution.dailyTemperatures([30, 40, 50, 60])
print("--------")
solution.dailyTemperatures([30, 60, 90])
print("---------")
solution.dailyTemperatures([60, 30, 90, 60])
