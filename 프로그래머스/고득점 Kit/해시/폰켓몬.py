def solution(nums):
    if len(set(nums)) > (len(nums) // 2):
        return len(nums) // 2
    else:
        return len(set(nums))
