def solution(nums):
    cnt = len(nums) // 2
    if cnt >= len(set(nums)):
        answer = len(set(nums))
    else:
        answer = cnt

    return answer
