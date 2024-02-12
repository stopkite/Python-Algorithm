class Solution:
    def longestConsecutive(self, nums):
        longest = 0
        num_dict = {}
        for num in nums:
            num_dict[num] = True

        for num in num_dict:
            # 이전 숫자가 존재하지 않으면 개수를 1로 초기화한다.
            if num - 1 not in num_dict:
                cnt = 1
                target = num + 1
                # 다음 숫자가 존재할 때까지 개수를 1증가
                while target in num_dict:
                    target += 1
                    cnt += 1
                # 연속된 숫자 개수 최댓값을 업데이트
                longest = max(longest, cnt)

        return longest


solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
# print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
