def solution(arr):
    count_dict = {}
    for num in arr:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    answer = []
    for cnt in count_dict.values():
        if cnt > 1:
            answer.append(cnt)

    if not answer:
        return [-1]
    else:
        return answer

print(solution([1, 2, 3, 3, 3, 3, 4, 4]))
print(solution([3, 2, 4, 4, 2, 5, 2, 5, 5]))
print(solution([3, 5, 7, 9, 1]))
